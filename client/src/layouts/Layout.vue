<template>
  <q-layout view="lHh Lpr lFf">
    <q-layout-header>
      <q-toolbar
        color="primary"
        :glossy="$q.theme === 'ios'"
        :inverted="$q.theme === 'ios'"
      >
        <q-toolbar-title>
          <router-link to="/" class="title">ohia.ai</router-link>
          <div slot="subtitle">
            Helping to identify native and invasive plants in Hawaii
          </div>
        </q-toolbar-title>
      </q-toolbar>
    </q-layout-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-layout-footer>
      <q-toolbar color="secondary" inverted>
        <div class="nav-bar">
          <q-btn flat round dense class="button"
            size="lg" icon="spa" to="/" />
          <CameraButton
            v-bind:button="{
              flat: true,
              round: true,
              dense: true,
              class: 'button',
              size: 'lg',
              icon: 'camera_alt',
            }"
          />
          <q-btn flat round dense class="button"
            size="lg" icon="help" to="/help" />
        </div>
      </q-toolbar>
    </q-layout-footer>
  </q-layout>
</template>

<script>
import CameraButton from '../components/PlantIdentification/CameraButton';

export default {
  name: 'Layout',
  components: {
    CameraButton,
  },
};
</script>

<style>
.title {
  text-decoration: none;
  color: white;
}
.button {
  margin-right: 90px;
}
.nav-bar {
  padding-left: 14px;
  display: flex;
  justify-content: space-around;
}
</style>
