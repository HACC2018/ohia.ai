<template>
  <div>
    <q-card>
      <q-card-title>
        Story
      </q-card-title>

      <q-card-separator />

      <q-card-main v-if="story">
        {{ story }}
      </q-card-main>

      <q-card-main v-else>
        No story provided.
      </q-card-main>
    </q-card>
  </div>
</template>

<script>
export default {
  props: {
    story: {
      type: String,
    },
  },
};
</script>

<style>

</style>
