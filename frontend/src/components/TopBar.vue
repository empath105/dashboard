<template>
  <header class="top-header">
    <div class="math-bg-overlay">
      <svg viewBox="0 0 1000 100" preserveAspectRatio="none">
        <path d="M-50,20 Q150,-10 350,40 T750,20 T1150,50" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="2.5" />
        <path d="M-50,35 Q180,5 380,55 T780,35 T1180,65" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2" />
        <path d="M-50,50 Q210,20 410,70 T810,50 T1210,80" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1.5" />

        <path d="M-150,80 Q250,40 550,90 T1050,40 T1550,70" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2.5" />
        <path d="M-150,65 Q280,25 580,75 T1080,25 T1580,55" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="2" />
        <path d="M-150,50 Q310,10 610,60 T1110,10 T1610,40" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="1.5" />

        <path d="M-100,10 Q200,80 500,20 T1100,80" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="3" />
      </svg>
    </div>

    <div class="header-left">
      <h1 class="header-title">
        Dashboard: <span class="model-name">{{ pageTitle }}</span>
      </h1>
    </div>

    <div class="header-right">
      <button class="action-arrow-btn" @click="handleArrowClick" title="Следующая модель">
        <div class="arrow-wrapper">
          <span class="arrow-shaft"></span>
          <i class="arrow-head"></i>
        </div>
      </button>
    </div>
  </header>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const pageTitle = computed(() => (route.meta.title as string) || 'SIR Модель');

  const emit = defineEmits(['arrow-click']);
  const handleArrowClick = () => emit('arrow-click');
</script>

<style scoped>
  .top-header {
    position: relative;
    background: linear-gradient(135deg, #6995D0 0%, #5581ba 100%);
    height: 70px;
    padding: 0 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 20px rgba(105, 149, 208, 0.25);
    color: #ffffff;
    overflow: hidden;
  }

  .math-bg-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }

  .math-bg-overlay svg {
    width: 100%;
    height: 100%;
    opacity: 0.8;
    animation: waveMotion 20s ease-in-out infinite alternate;
  }

  @keyframes waveMotion {
    0% {
      transform: scaleY(1) skewX(0deg);
    }
    50% {
      transform: scaleY(1.08) skewX(1deg);
    }
    100% {
      transform: scaleY(0.95) skewX(-1deg);
    }
  }

  .header-left {
    z-index: 1;
  }

  .header-title {
    margin: 0;
    font-size: 22px;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.85);
    letter-spacing: -0.3px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .model-name {
    color: #ffffff;
    font-weight: 700;
  }

  .header-right {
    z-index: 1;
  }

  .action-arrow-btn {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 50%;
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    position: relative;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .arrow-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    width: 100%;
    height: 100%;
  }

  .arrow-shaft {
    width: 12px;
    height: 2px;
    background-color: #ffffff;
    display: inline-block;
    transform: translateX(2px);
    transition: all 0.3s ease;
  }

  .arrow-head {
    border: solid #ffffff;
    border-width: 0 2px 2px 0;
    display: inline-block;
    padding: 3px;
    transform: rotate(-45deg) translateX(-1px);
    transition: all 0.3s ease;
  }

  .action-arrow-btn:hover {
    background: #ffffff;
    border-color: #ffffff;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
  }

    .action-arrow-btn:hover .arrow-shaft {
      background-color: #5581ba;
      transform: translateX(4px);
    }

    .action-arrow-btn:hover .arrow-head {
      border-color: #5581ba;
    }

  .action-arrow-btn:active {
    transform: scale(0.92);
  }
</style>
