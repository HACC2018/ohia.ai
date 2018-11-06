<template>
  <q-page
    padding
  >
    <template v-if="imageSrc">
      <q-btn
        @click="viewPlantIdentification"
      >
        <q-icon name="keyboard_arrow_left" />
        Results
      </q-btn>
    </template>
    <template v-else>
      <q-btn
        @click="goToPreviousPage"
      >
        <q-icon name="keyboard_arrow_left" />
        Previous Page
      </q-btn>
    </template>
    <br />
    <br />
    <div
      class="row gutter-md"
    >
      <div
        class="col-xs-12 col-sm-12 col-md-12 col-lg-4"
      >
        <plant-information
          :image="image"
          :genus="genus"
          :species="species"
          :plant_name="plant_name"
          :common_name="common_name"
          :hawaiian_name="hawaiian_name"
          :scientific_name="scientific_name"
          :endangered="endangered"
          :status="status"
          :description="description"
        />
      </div>

      <div
        class="col-xs-12 col-sm-12 col-md-12 col-lg-8"
      >
        <plant-story
          :story="story"
        />

        <br />

        <plant-uses
          :uses="uses"
        />

        <br />

        <plant-uploads
          :image="image"
          :id="$route.params.id"
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
  props: {
    imageId: {
      type: Number,
    },
    imageSrc: {
      type: String,
    },
    predictions: {
      type: Array,
    },
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
      endangered: '',
      image: '',
    };
  },
  methods: {
    goToPreviousPage() {
      this.$router.go(-1);
    },
    viewPlantIdentification() {
      this.$router.push({
        name: 'identify',
        params: {
          imageIdProp: this.imageId,
          imageSrcProp: this.imageSrc,
          predictionsProp: this.predictions,
        },
      });
    },
    fetchPlantDetails() {
      const plantUrl = `${process.env.API_HOST}/api/plant/${this.$route.params.id}`;
      this.$axios
        .get(plantUrl)
        .then((response) => {
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
          this.endangered = data.endangered;
        })
        .then(() => {
          const plantImageUrl = `${process.env.API_HOST}/api/images/single/${this.$route.params.id}`;
          this.$axios
            .get(plantImageUrl)
            .then((response) => {
              this.fetching = false;
              const { data } = response;
              // eslint-ignore-next-line
              this.image = data ? data.image_url : '';
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
