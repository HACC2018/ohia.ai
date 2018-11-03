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
          <plant-candidate :prediction="pred" />
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
    predictions: {
      type: Array,
    },
  },
};
</script>

<style>
</style>
