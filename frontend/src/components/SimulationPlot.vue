<template>
  <div class="plot-container">
    <div id="sir-plot" class="plot-canvas"></div>
  </div>
</template>

<script setup lang="ts">
import { watch, onMounted } from 'vue';
import Plotly from 'plotly.js-dist-min';

interface Point {
  x: number;
  y: number;
  val: number;
}

const props = withDefaults(
  defineProps<{
    points: Point[];
    zmin?: number;
    zmax?: number;
    step?: number;
    xmin?: number;
    xmax?: number;
  }>(),
  {
    zmin: 0,
    zmax: 1,
    step: 0.05,
    xmin: 0,
    xmax: 100
  }
);

const drawPlot = (points: Point[]) => {
  if (points.length <= 3) return;

  const plotData = [{
    x: points.map(p => p.x),
    y: points.map(p => p.y),
    z: points.map(p => p.val),
    type: 'contour',
    colorscale: 'Jet',
    zmin: props.zmin,
    zmax: props.zmax,
    autocontour: false,
    contours: {
      start: props.zmin,
      end: props.zmax,
      size: props.step
    },
    colorbar: {
      x: 1.02,           
      xanchor: 'left',   
      xref: 'x',         
      thickness: 20,     
      len: 1 
    }
  }];

  const layout = {
    title: {
      text: 'Динамика распространения',
      font: { size: 16, color: '#334155', weight: '600' }
    },
    uirevision: 'true',
    responsive: true,
    autosize: true,
    displayModeBar: false,
    xaxis: {
      scaleanchor: 'y',
      scaleratio: 1,
      automargin: true,
      autorange: false,
      range: [props.xmin, props.xmax],
      showgrid: false,
      zeroline: false,
      constrain: 'domain'
    },
    yaxis: {
      automargin: true,
      autorange: false,
      range: [props.xmin, props.xmax],
      showgrid: false,
      zeroline: false,
      constrain: 'domain'
    },
    margin: { l: 60, r: 80, t: 60, b: 60 },
    paper_bgcolor: 'rgba(0,0,0,0)', 
    plot_bgcolor: 'rgba(0,0,0,0)'   
  };

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  Plotly.react('sir-plot', plotData as any, layout as any);
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
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .plot-canvas {
    width: 100%;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
  }
</style>
