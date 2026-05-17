<template>
  <div class="plot-container">
    <div id="sir-plot" class="plot-canvas"></div>
  </div>
</template>

<script setup lang="ts">
import { watch, onMounted } from 'vue';
import Plotly from 'plotly.js-dist-min';

interface SirPoint {
  x: number;
  y: number;
  val: number;
}

const props = defineProps<{
  points: SirPoint[];
}>();

const drawPlot = (points: SirPoint[]) => {
  if (points.length <= 3) return;

  const plotData = [{
    x: points.map(p => p.x),
    y: points.map(p => p.y),
    z: points.map(p => p.val),
    type: 'contour',
    colorscale: 'Jet',
    zmin: 0,
    zmax: 1,
    autocontour: false,
    contours: { start: 0, end: 1, size: 0.05 }
  }];

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  Plotly.react('sir-plot', plotData as any, {
    title: 'Динамика распространения (Live)',
    uirevision: 'true',
    responsive: true,
    autosize: true,
    displayModeBar: false
  });
};

onMounted(() => {
  Plotly.newPlot('sir-plot', [], { title: 'Ожидание запуска...' }, { responsive: true });
});

watch(() => props.points, (newPoints) => {
  drawPlot(newPoints);
}, { deep: true });
</script>


<style scoped>
  .plot-container {
    height: 70vh;
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    padding: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    overflow: hidden;
  }
  .plot-container:hover {
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
  }

  .plot-canvas {
    width: 100%;
    height: 100%;
    max-width: 100%;
  }
</style>
