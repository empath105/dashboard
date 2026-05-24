<template>
  <div class="dashboard-layout">
    <aside class="layout-sidebar">
      <TuringParams v-model="params"
                  :loading="loading"
                  @calculate="runSimulation" />
    </aside>

    <main class="layout-main">
      <SimulationPlot :points="sharedPoints"
                      :zmin="0"
                      :zmax="5"
                      :step="0.25"
                      :xmin="0"
                      :xmax="1"/>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, nextTick } from 'vue';
import TuringParams from 'components/TuringParams.vue';
import SimulationPlot from 'components/SimulationPlot.vue';

interface Point {
  x: number;
  y: number;
  val: number;
}

const loading = ref(false);
const sharedPoints = ref<Point[]>([]);

const params = reactive({
  a: 0.1,
  b: 0.9,
  Du: 0.001,
  Dv: 0.04,
  tmax: 140
});

const runSimulation = async () => {
  loading.value = true;
  sharedPoints.value = [];

  const url = `http://127.0.0.1:8000/api/run_turing/?a=${params.a}&b=${params.b}&Du=${params.Du}&Dv=${params.Dv}&tmax=${params.tmax}`;

  try {
    const response = await fetch(url);
    const reader = response.body?.getReader();
    const decoder = new TextDecoder();

    let currentPoints: Point[] = [];
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
    display: flex;
    gap: 24px;
    padding: 24px;
    align-items: start;
    justify-content: flex-start;
    min-height: 100%;
    box-sizing: border-box;
    background: #f8fafc;
  }

  .layout-sidebar {
    width: 350px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
  }

  .layout-main {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    padding: 24px;
    height: 80vh;
    width: 90vh;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  @media (max-width: 992px) {
    .dashboard-layout {
      flex-direction: column;
      gap: 16px;
      padding: 16px;
    }

    .layout-sidebar {
      width: 100%;
    }

    .layout-main {
      width: 100%;
      height: 550px;
    }
  }
</style>
