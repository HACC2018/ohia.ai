<template>
  <div>
    <q-card>
      <q-card-title>
        Uses
      </q-card-title>

      <q-card-separator />

      <q-card-main>
        {{ uses }}
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
