<template>
  <q-page padding>
    <div class="row">
      <div class="col-sm-12 col-md-4 q-mr-md q-mb-md">
        <PlantInformation></PlantInformation>
      </div>

      <div class="col-sm-12 col-md-7">
        <PlantStory class="q-mb-md"></PlantStory>

        <PlantUses class="q-mb-md"></PlantUses>

        <PlantUploads class="q-mb-md"></PlantUploads>
      </div>
    </div>
  </q-page>
</template>

<script>
import PlantInformation from '../components/PlantDetails/PlantInformation';
import PlantStory from '../components/PlantDetails/PlantStory';
import PlantUses from '../components/PlantDetails/PlantUses';
import PlantUploads from '../components/PlantDetails/PlantUploads';

export default {
  components: {
    PlantInformation,
    PlantStory,
    PlantUses,
    PlantUploads,
  },
};
</script>

<style>

</style>
