<template>
  <q-page
    padding
  >
    {{ loaded }}
    <div v-if="loaded">
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
    </div>
  </q-page>
</template>

<script>
import CapturedImage from '../components/PlantIdentification/CapturedImage';
import MoreAbout from '../components/PlantIdentification/MoreAbout';

export default {
  name: 'PlantIdentification',
  components: {
    CapturedImage,
    MoreAbout,
  },
  props: {
    loaded: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      imageSrc: '',
    };
  },
};
</script>

<style>
</style>
