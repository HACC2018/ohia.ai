<template>
  <q-page
    padding
  >
    <div
      class="row"
    >
      <div
        class="col-md-12 col-lg-4 q-mr-md q-mb-md"
      >
        <PlantInformation />
      </div>

      <div
        class="col-md-12 col-lg-7"
      >
        <PlantStory
          class="q-mb-md"
        />

        <PlantUses
          class="q-mb-md"
        />

        <PlantUploads
          class="q-mb-md"
        />
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
