<template>
  <q-card>
    <q-card-title>
      Plant Identification Results
    </q-card-title>

    <q-card-separator />
    <div class="image-background">
      <img :src="imageSrc" class="image" />
    </div>
    <q-card-separator />

    <q-card-main>Classify the plant above:</q-card-main>
    <q-card-separator />

    <q-card-actions align="center">
      <template v-for="pred in predictions">
        <q-btn
          v-bind:key="pred.id"
          flat
          :color="pred.color"
          @click="classifyPlant(pred.id, null)"
        >
          {{ pred.className }}
        </q-btn>
      </template>
      <q-btn @click="classifyPlant(null, null)" flat>I don't know</q-btn>
    </q-card-actions>

    <q-card-separator />

    <div class="guess-block">
      <q-input
        class="q-ma-md"
        v-model="userGuess"
        float-label="Or enter the plant name if you know it"
      />
      <div align="right" class="guess-submit">
        <q-btn
          flat
          color="secondary"
          @click="classifyPlant(null, userGuess)"
        >
          Submit Name
        </q-btn>
      </div>
    </div>
  </q-card>
</template>

<script>
export default {
  name: 'CapturedImage',
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
      userGuess: '',
    };
  },
  methods: {
    classifyPlant(plantId, userGuess) {
      const appHost = 'http://localhost:3000';
      const imageUpdateUrl = `${appHost}/api/plant-image/${this.imageId}`;
      this.$axios.put(imageUpdateUrl, {
        plant_id: plantId,
        identified: !!plantId,
        user_guess: userGuess,
      })
        .then(() => {
          // const todo = res.data.plantImage;
        })
        .catch((err) => {
          console.error('Error updating plant image data:', err);
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Classifying plant failed',
            icon: 'report_problem',
          });
        });
    },
  },
};
</script>

<style>
.guess-block {
  padding-bottom: 10px;
}
.guess-submit {
  padding-right: 16px;
}
.image-background {
  background: #E6E6E6;
}
.image {
  width: auto;
  height: 270px;
  display: block;
  margin: 0 auto;
}
</style>
