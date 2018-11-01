<template>
  <div>
    <q-card>
      <q-card-title>
        Uses
      </q-card-title>

      <q-card-separator />

      <q-card-main>
        <q-list no-border>
          <q-item>
            <q-item-main
            label="Eating"
            sublabel="Its great taste made it suitable for eating."
          />
          </q-item>
          <q-item-separator />
          <q-item>
            <q-item-main
            label="Cleaning"
            sublabel="Its great cleaning powers were used."
          />
          </q-item>
          <q-item>
            <q-item-main
              label="Medicine"
              sublabel="Its great healing powers were used."
            />
          </q-item>
        </q-list>
      </q-card-main>
    </q-card>
  </div>
</template>

<script>
export default {
  props: {
    uses: {
      type: Array,
    },
  },
};
</script>

<style>

</style>
