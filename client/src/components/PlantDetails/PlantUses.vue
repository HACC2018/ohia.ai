<template>
  <div>
    <q-card>
      <q-card-title>
        Uses
      </q-card-title>

      <q-card-separator />

      <q-card-main v-if="uses">
        {{ uses }}
      </q-card-main>

      <q-card-main v-else>
        No uses provided.
      </q-card-main>
    </q-card>
  </div>
</template>

<script>
export default {
  props: {
    uses: {
      type: String,
    },
  },
};
</script>

<style>

</style>
