<template>
  <q-card>
    <q-card-title>
      More about...
    </q-card-title>

    <q-card-separator />

    <div
      class="row"
    >
      <template v-for="pred in predictions">
        <div
          v-bind:key="pred.id"
          class="col-lg-4"
        >
          <plant-candidate
            :imageId="imageId"
            :imageSrc="imageSrc"
            :predictions="predictions"
            :prediction="pred"
          />
        </div>
      </template>
    </div>
  </q-card>
</template>

<script>
import PlantCandidate from './PlantCandidate';

export default {
  name: 'MoreAbout',
  components: {
    PlantCandidate,
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
};
</script>

<style>
</style>
