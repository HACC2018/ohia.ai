<template>
  <q-page padding>
    <div class="row gutter-sm">
      <div class="col-sm-12 col-md-6">
        <Stepper />
      </div>
      <div class="col-sm-12 col-md-6">
        <plant-detection class="" />
      </div>
    </div>
    <br />
    <plant-directory />
    <br />
  </q-page>
</template>

<style>
</style>

<script>
import PlantDetection from './PlantDetection';
import Stepper from '../components/Home/Stepper';
import PlantDirectory from '../components/Home/PlantDirectory';

export default {
  name: 'PageIndex',
  components: {
    PlantDetection,
    Stepper,
    PlantDirectory,
  },
};
</script>
