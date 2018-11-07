<template>
  <q-card>
    <q-card-media>
      <img
        :src="image"
      >
    </q-card-media>

    <q-card-title>
      {{ plant_name }}

      <div
        slot="right"
        class="row items-center"
      >
        <span>
          {{ status }}
        </span>
        <span>・</span>
        <span
          :class="{
            'text-red': endangered === 'Endangered' ? true : null,
            'text-pink': endangered === 'Threatened' ? true : null,
            'text-deep-orange': endangered === 'Candidate for listing'? true : null,
            'text-orange': endangered === 'Species of concern'? true : null,
            'text-green': endangered === 'Not listed by state' ? true : null,
          }"
        >
          {{ endangered }}
        </span>
      </div>
    </q-card-title>

    <q-card-separator />

    <q-card-main>
      <p v-if="genus">
        <span>
          Genus・
        </span>

        <span class="text-faded">
          {{ genus }}
        </span>
      </p>

      <p v-if="species">
        <span>
          Species・
        </span>

        <span class="text-faded">
          {{ species }}
        </span>
      </p>

      <p v-if="common_name">
        <span>
          Common Name・
        </span>

        <span class="text-faded">
          {{ common_name }}
        </span>
      </p>

      <p v-if="hawaiian_name">
        <span>
          Hawaiian Name・
        </span>

        <span class="text-faded">
          {{ hawaiian_name }}
        </span>
      </p>

      <p v-if="scientific_name">
        <span>
          Scientific Name・
        </span>

        <span class="text-faded">
          {{ scientific_name }}
        </span>
      </p>

      <p v-if="description">
        <span>
          Description・
        </span>

        <span class="text-faded">
          {{ description }}
        </span>
      </p>
    </q-card-main>
  </q-card>
</template>

<script>
export default {
  props: {
    image: {
      type: String,
    },
    genus: {
      type: String,
    },
    species: {
      type: String,
    },
    plant_name: {
      type: String,
    },
    common_name: {
      type: String,
    },
    hawaiian_name: {
      type: String,
    },
    scientific_name: {
      type: String,
    },
    status: {
      type: String,
    },
    description: {
      type: String,
    },
    endangered: {
      type: String,
    },
  },
};
</script>

<style>

</style>
