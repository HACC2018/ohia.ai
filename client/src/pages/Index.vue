<template>
  <q-page class="flex flex-center">
    <plant-detection />
  </q-page>
</template>

<style>
</style>

<script>
import PlantDetection from './PlantDetection';

export default {
  name: 'PageIndex',
  components: {
    PlantDetection,
  },
};
</script>
