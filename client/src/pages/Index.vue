<template>
  <q-page>
    <q-card-title>Browse the flora of Hawaii</q-card-title>
    <q-card-separator />
    <plant-directory />
  </q-page>
</template>

<script>
import PlantDirectory from '../components/Home/PlantDirectory';

export default {
  name: 'PageIndex',
  components: {
    PlantDirectory,
  },
};
</script>

<style>
</style>
