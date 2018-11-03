<template>
  <q-page
    padding
  >
    <div
      class="row gutter-md"
    >
      <div
        class="col-md-12 col-lg-4"
      >
        <PlantInformation />
      </div>

      <div
        class="col-md-12 col-lg-8"
      >
        <PlantStory />

        <br />

        <PlantUses />

        <br />

        <PlantUploads />
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
  methods: {
    fetchPlantDetails() {
      this.$axios
        .get(`http://localhost:3000/api/plant/${this.$route.params.id}`)
        .then((response) => {
          console.log(response);
        });
    },
  },
  mounted() {
    this.fetchPlantDetails();
  },
};
</script>

<style>

</style>
