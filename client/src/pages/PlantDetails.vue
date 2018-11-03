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
        <plant-information
          :genus="genus"
          :species="species"
          :plant_name="plant_name"
          :common_name="common_name"
          :hawaiian_name="hawaiian_name"
          :scientific_name="scientific_name"
          :status="status"
          :description="description"
        />
      </div>

      <div
        class="col-md-12 col-lg-8"
      >
        <plant-story
          :story="story"
        />

        <br />

        <plant-uses
          :uses="uses"
        />

        <br />

        <plant-uploads />
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
  data() {
    return {
      fetching: true,
      genus: '',
      species: '',
      plant_name: '',
      common_name: '',
      hawaiian_name: '',
      scientific_name: '',
      status: '',
      description: '',
      story: '',
      uses: '',
    };
  },
  methods: {
    fetchPlantDetails() {
      this.$axios
        .get(`http://localhost:3000/api/plant/${this.$route.params.id}`)
        .then((response) => {
          this.fetching = false;
          const { data } = response;

          this.genus = data.genus;
          this.species = data.species;
          this.plant_name = data.plant_name;
          this.common_name = data.common_name;
          this.hawaiian_name = data.hawaiian_name;
          this.scientific_name = data.scientific_name;
          this.status = data.status;
          this.description = data.description;
          this.story = data.story;
          this.uses = data.uses;
        })
        .then(() => {
          this.$axios
            .get(`http://localhost:3000/api/${this.$route.params.id}`)
            .then(() => {
            });
        })
        .catch((err) => {
          this.fetching = false;
          console.log(err);
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
