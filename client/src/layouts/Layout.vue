<template>
  <q-layout view="lHh Lpr lFf">
    <q-layout-header>
      <q-toolbar
        color="primary"
        :glossy="$q.theme === 'ios'"
        :inverted="$q.theme === 'ios'"
      >
        <router-link to="/" class="title">
          <img src="statics/ohia.ai_logo.svg" class="logo" />
        </router-link>
        <q-toolbar-title>
          <router-link to="/" class="title">ohia.ai</router-link>
          <div slot="subtitle">
            Helping to identify native and invasive plants in Hawaiʻi
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
          <CameraButton
            mode="library"
            v-bind:button="{
              flat: true,
              round: true,
              dense: true,
              class: 'button',
              size: 'lg',
              icon: 'image_search',
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
.logo {
  width: 36px;
  height: 36px;
}
.title {
  text-decoration: none;
  color: white;
}
.button {
  margin-right: 54px;
}
.nav-bar {
  display: flex;
  justify-content: space-around;
}
</style>
