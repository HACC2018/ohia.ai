<template>
  <q-page
    padding
  >
    <div
      class="row gutter-sm"
    >
      <div
        class="col-sm-12 col-md-4"
      >
        <captured-image />
      </div>
      <div
        class="col-sm-12 col-md-8"
      >
        <more-about />
      </div>
    </div>
  </q-page>
</template>

<script>
import CapturedImage from '../components/PlantIdentification/CapturedImage';
import MoreAbout from '../components/PlantIdentification/MoreAbout';

export default {
  components: {
    CapturedImage,
    MoreAbout,
  },
};
</script>

<style>

</style>
