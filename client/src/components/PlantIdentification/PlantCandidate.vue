<template>
<q-card-main>
  <q-card>
    <q-card-media
      overlay-position="top"
      v-if="prediction.plantImages && prediction.plantImages.length > 0"
    >
      <img
        :src="prediction.plantImages[0].image_url"
      >
    </q-card-media>

    <q-card-title class="relative-position">
      <q-btn
        :color="prediction.color"
        :label="this.formatPercentage()"
        class="absolute"
        style="top: 0; right: 8px; transform: translateY(-50%);"
        no-ripple
      />
    </q-card-title>

    <q-card-actions
      class="q-pa-md"
      align="center"
    >
      <q-btn
        flat
        :to="`/plant/${prediction.id}`"
      >
        {{ prediction.className }}
        <q-icon
          name="keyboard_arrow_right"
        />
      </q-btn>
    </q-card-actions>
  </q-card>
</q-card-main>
</template>

<script>
export default {
  name: 'PlantCandidate',
  props: {
    prediction: {
      type: Object,
    },
  },
  methods: {
    formatPercentage() {
      return `${Math.round(this.prediction.probability * 100)}%`;
    },
    viewPlantDetails() {
      // TODO
    },
  },
};
</script>

<style>
</style>
