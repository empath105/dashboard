<template>
  <div class="app-layout">
    <TopBar class="dashboard-header" />

    <main class="page-body">
      <router-view v-slot="{ Component, route }">
        <transition :name="transitionName" mode="out-in">
          <component :is="Component" :key="route.path" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import TopBar from 'components/TopBar.vue';

const route = useRoute();

const transitionName = ref('slide-left');

watch(
  () => route.meta.index,
  (newIndex, oldIndex) => {
    if (newIndex && oldIndex) {
      transitionName.value = (newIndex as number) > (oldIndex as number) ? 'slide-left' : 'slide-right';
    }
  }
);
</script>

<style>
  body, html {
    margin: 0;
    padding: 0;
    font-family: system-ui, -apple-system, sans-serif;
    background-color: #f8fafc;
    overflow: hidden;
  }

  .app-layout {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
  }

  .dashboard-header {
    width: 100%;
    flex-shrink: 0;
  }

  .page-body {
    flex-grow: 1;
    position: relative;
    overflow-x: hidden; 
    overflow-y: auto; 
  }

  .slide-left-enter-active,
  .slide-left-leave-active,
  .slide-right-enter-active,
  .slide-right-leave-active {
    transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.35s ease;
  }

  .slide-left-enter-from {
    transform: translateX(100%);
    opacity: 0;
  }

  .slide-left-leave-to {
    transform: translateX(-100%);
    opacity: 0;
  }

  .slide-right-enter-from {
    transform: translateX(-100%);
    opacity: 0;
  }

  .slide-right-leave-to {
    transform: translateX(100%);
    opacity: 0;
  }
</style>
