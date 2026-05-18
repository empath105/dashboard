<template>
  <div class="dashboard-layout">
    <aside class="layout-sidebar">
      <SIRParams v-model="params"
                 :loading="loading"
                 @calculate="runSimulation" />
    </aside>

    <main class="layout-main">
      <SimulationPlot :points="sharedPoints" />
    </main>
  </div>
</template>

<script setup lang="ts">
  import { ref, reactive, nextTick } from 'vue';
  import SIRParams from 'components/SIRParams.vue';
  import SimulationPlot from 'components/SimulationPlot.vue';

  interface SirPoint {
    x: number;
    y: number;
    val: number;
  }

  const loading = ref(false);
  const sharedPoints = ref<SirPoint[]>([]);

  const params = reactive({
    beta: 0.4,
    gamma: 0.1,
    ds: 2.0,
    di: 0.5,
    dr: 2.0,
    tmax: 100
  });

  const runSimulation = async () => {
    loading.value = true;
    sharedPoints.value = [];

    const url = `http://127.0.0.1:8000/api/run_sir/?beta=${params.beta}&gamma=${params.gamma}&di=${params.di}&ds=${params.ds}&dr=${params.dr}&tmax=${params.tmax}`;

    try {
      const response = await fetch(url);
      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      let currentPoints: SirPoint[] = [];
      let buffer = '';
      let isRendering = false;

      while (true) {
        const { value, done } = await reader!.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          const cleanLine = line.replace('data: ', '').trim();

          if (cleanLine === 'FRAME_START') {
            currentPoints = [];
          } else if (cleanLine === 'FRAME_END') {
            if (!isRendering) {
              isRendering = true;

              sharedPoints.value = [...currentPoints];

              void nextTick(() => {
                isRendering = false;
              });
            }
          } else if (cleanLine !== '') {
            const parts = cleanLine.split(' ');
            if (parts.length === 3) {
              const x = parseFloat(parts[0] ?? "");
              const y = parseFloat(parts[1] ?? "");
              const val = parseFloat(parts[2] ?? "");

              if (!isNaN(x) && !isNaN(y) && !isNaN(val)) {
                currentPoints.push({ x, y, val });
              }
            }
          }
        }
      }
    } catch (error) {
      console.error('Ошибка стриминга:', error);
    } finally {
      loading.value = false;
    }
  };
</script>

<style scoped>
  .dashboard-layout {
    display: grid;
    grid-template-columns: 350px 1fr;
    gap: 24px;
    padding: 24px;
    align-items: start;
  }

  .layout-sidebar {
    display: flex;
    flex-direction: column;
  }

  .layout-main {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    padding: 24px;
    min-height: 500px;
    max-width: 55vw;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  @media (max-width: 992px) {
    .dashboard-layout {
      grid-template-columns: 1fr;
      gap: 16px;
      padding: 16px;
    }
  }
</style>
