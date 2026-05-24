<template>
  <div class="params-container">
    <h3 class="params-title">Параметры модели Ф-КПП</h3>

    <div class="params-group">
      <div class="param-item">
        <div class="param-header">
          <span>Пролиферация клеток (B)</span>
          <span class="param-value value-red">{{ localParams.B }}</span>
        </div>
        <input type="range" v-model.number="localParams.B" min="0.1" max="2.0" step="0.1" class="custom-slider"
               :style="{ background: `linear-gradient(to right, #e53935 0%, #e53935 ${((localParams.B - 0.1) / (2.0 - 0.1)) * 100}%, #e0e0e0 ${((localParams.B - 0.1) / (2.0 - 0.1)) * 100}%, #e0e0e0 100%)` }" />
      </div>

      <div class="param-item">
        <div class="param-header">
          <span>Потребление питания (q)</span>
          <span class="param-value value-green">{{ localParams.q }}</span>
        </div>
        <input type="range" v-model.number="localParams.q" min="0.1" max="1.5" step="0.1" class="custom-slider"
               :style="{ background: `linear-gradient(to right, #4caf50 0%, #4caf50 ${((localParams.q - 0.1) / (1.5 - 0.1)) * 100}%, #e0e0e0 ${((localParams.q - 0.1) / (1.5 - 0.1)) * 100}%, #e0e0e0 100%)` }" />
      </div>

      <div class="param-item">
        <div class="param-header">
          <span>Подвижность клеток (Da)</span>
          <span class="param-value value-blue">{{ localParams.Da }}</span>
        </div>
        <input type="range" v-model.number="localParams.Da" min="0.1" max="3.0" step="0.1" class="custom-slider"
               :style="{ background: `linear-gradient(to right, #2196f3 0%, #2196f3 ${((localParams.Da - 0.1) / (3.0 - 0.1)) * 100}%, #e0e0e0 ${((localParams.Da - 0.1) / (3.0 - 0.1)) * 100}%, #e0e0e0 100%)` }" />
      </div>

      <div class="param-item">
        <div class="param-header">
          <span>Диффузия питания (Ds)</span>
          <span class="param-value value-purple">{{ localParams.Ds }}</span>
        </div>
        <input type="range" v-model.number="localParams.Ds" min="3000" max="6000" step="200" class="custom-slider"
               :style="{ background: `linear-gradient(to right, #9c27b0 0%, #9c27b0 ${((localParams.Ds - 3000) / (6000 - 3000)) * 100}%, #e0e0e0 ${((localParams.Ds - 3000) / (6000 - 3000)) * 100}%, #e0e0e0 100%)` }" />
      </div>

      <div class="param-item">
        <div class="param-header">
          <span>Порог голодания (Scrit)</span>
          <span class="param-value value-orange">{{ localParams.Scrit }}</span>
        </div>
        <input type="range" v-model.number="localParams.Scrit" min="0.1" max="0.6" step="0.05" class="custom-slider"
               :style="{ background: `linear-gradient(to right, #ff9800 0%, #ff9800 ${((localParams.Scrit - 0.1) / (0.6 - 0.1)) * 100}%, #e0e0e0 ${((localParams.Scrit - 0.1) / (0.6 - 0.1)) * 100}%, #e0e0e0 100%)` }" />
      </div>

      <div class="param-item">
        <div class="param-header">
          <span>Срок прогноза (шагов)</span>
          <span class="param-value value-grey">{{ localParams.tmax }}</span>
        </div>
        <input type="range" v-model.number="localParams.tmax" min="10" max="60" step="5" class="custom-slider"
               :style="{ background: `linear-gradient(to right, #757575 0%, #757575 ${((localParams.tmax - 10) / (60 - 10)) * 100}%, #e0e0e0 ${((localParams.tmax - 10) / (60 - 10)) * 100}%, #e0e0e0 100%)` }" />
      </div>
    </div>

    <button class="calculate-btn" :disabled="loading" @click="$emit('calculate')">
      <span v-if="!loading">Рассчитать</span>
      <span v-else class="spinner"></span>
    </button>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  modelValue: {
    B: number;
    q: number;
    Da: number;
    Ds: number;
    Scrit: number;
    tmax: number;
  };
  loading: boolean;
}>();

const emit = defineEmits(['update:modelValue', 'calculate']);

const localParams = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
});
</script>

<style scoped>
  .params-container {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .params-title {
    margin: 0;
    font-size: 20px;
    font-weight: 600;
    color: #333333;
    border-bottom: 2px solid #6995D0;
    padding-bottom: 8px;
  }

  .params-group {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .param-item {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .param-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    font-weight: 500;
    color: #555555;
  }

  .param-value {
    font-weight: bold;
    padding: 2px 6px;
    border-radius: 4px;
    background: #f5f5f5;
  }

  .value-red {
    color: #e53935;
  }

  .value-orange {
    color: #ff9800;
  }

  .value-green {
    color: #4caf50;
  }

  .value-blue {
    color: #2196f3;
  }

  .value-purple {
    color: #9c27b0;
  }

  .value-green-light {
    color: #8bc34a;
  }

  .value-grey {
    color: #757575;
  }

  .custom-slider {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 6px;
    border-radius: 3px;
    outline: none;
    cursor: pointer;
  }

  .custom-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: currentColor;
    border: 3px solid currentColor;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    transition: transform 0.1s ease;
  }

  .custom-slider::-moz-range-thumb {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: currentColor;
    border: 3px solid currentColor;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    transition: transform 0.1s ease;
  }

  .custom-slider::-webkit-slider-thumb:hover {
    transform: scale(1.2);
  }

  .custom-slider::-moz-range-thumb:hover {
    transform: scale(1.2);
  }

  .slider-red, .param-item:has(.value-red) .custom-slider {
    color: #e53935;
  }

  .param-item:has(.value-green) .custom-slider {
    color: #4caf50;
  }

  .param-item:has(.value-orange) .custom-slider {
    color: #ff9800;
  }

  .param-item:has(.value-blue) .custom-slider {
    color: #2196f3;
  }

  .param-item:has(.value-purple) .custom-slider {
    color: #9c27b0;
  }

  .param-item:has(.value-green-light) .custom-slider {
    color: #8bc34a;
  }

  .param-item:has(.value-grey) .custom-slider {
    color: #757575;
  }

  .calculate-btn {
    background: #6995D0;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 12px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s ease, transform 0.1s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 48px;
  }

  .calculate-btn:hover:not(:disabled) {
    background: #527bb3;
  }

  .calculate-btn:active:not(:disabled) {
    transform: scale(0.98);
  }

  .calculate-btn:disabled {
    background: #b0bec5;
    cursor: not-allowed;
  }

  .spinner {
    width: 20px;
    height: 20px;
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: #ffffff;
    animation: spin 1s ease-in-out infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
