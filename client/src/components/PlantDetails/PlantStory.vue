<template>
  <div>
    <q-card>
      <q-card-title>
        Story
      </q-card-title>

      <q-card-separator />

      <q-card-main>
        The legend says that one day Pele
        met a handsome warrior named Ohia
        and she asked him to marry her. Ohia,
        however, had already pledged his love
        to Lehua.  Pele was furious when Ohia
        turned down her marriage proposal, so
        she turned Ohia into a twisted tree.
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
