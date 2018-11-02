<template>
  <q-layout view="lHh Lpr lFf">
    <q-layout-header>
      <q-toolbar
        color="primary"
        :glossy="$q.theme === 'ios'"
        :inverted="$q.theme === 'ios'"
      >
        <q-toolbar-title>
          <router-link to="/" style="text-decoration: none; color: white;">ohia.ai</router-link>
          <div slot="subtitle">
            Helping to identify native and invasive plants in Hawaii.
          </div>
        </q-toolbar-title>
      </q-toolbar>
    </q-layout-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-layout-footer>
      <q-toolbar color="secondary" inverted>
        <div style="display: flex; justify-content: space-around;">
          <q-btn flat round dense style="margin-right: 28px;" 
            size="lg" icon="home" to="/" />
          <q-btn flat round dense style="margin-right: 28px;" 
            size="lg" icon="info" to="/about" />
          <q-btn flat round dense style="margin-right: 28px;" 
            size="lg" icon="camera_alt" to="/detector" />
          <q-btn flat round dense style="margin-right: 28px;" 
            size="lg" icon="spa" to="/plant" />
          <q-btn flat round dense style="margin-right: 28px;" 
            size="lg" icon="image_search" to="/identify" />
        </div>
      </q-toolbar>
    </q-layout-footer>
  </q-layout>
</template>

<script>
export default {
  name: 'Layout',
};
</script>

<style>
</style>
