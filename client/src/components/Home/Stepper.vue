<template>
  <div>
    <q-card>
      <q-card-title>
        Locating and identifying native and invasive plant species
      </q-card-title>

      <q-card-separator />

      <q-card-main>
        <q-timeline
          responsive
          color="primary"
        >
          <q-timeline-entry
            title="Allow us to use your camera and photos."
            side="right"
            subtitle="Step 1"
            icon="camera"
          >
            <div>
              To begin helping us identify plant species
              in Hawaiʻi, when prompted, allow this application
              access to your phone. If you choose to allow
              access and upload an image to this app,
              data about the image will be collected and stored,
              including the image itself and the time it was taken.
            </div>
          </q-timeline-entry>

          <q-timeline-entry
            title="Allow us to use your location."
            side="right"
            subtitle="Step 2"
            icon="place"
          >
            <div>
              In addition, we request that you allow us to store your
              location. When you take the image or upload an existing photo,
              your GPS location will be recorded to help the State of Hawaiʻi
              protect and track native plants and possibly eradicate invasive plants.
            </div>
          </q-timeline-entry>

          <q-timeline-entry
            title="Snap the image or upload an existing photo."
            side="right"
            subtitle="Step 3"
            icon="camera_alt"
          >
            <div>
              While taking the image of the plant, keep in mind:
              take photos that are close, in focus, and well-lit.
              If possible, frame only one plant species in your photo.
            </div>
          </q-timeline-entry>

          <q-timeline-entry
            title="Classify the plant."
            side="right"
            subtitle="Step 4"
            icon="sort_by_alpha"
          >
            <div>
              After taking the image or uploading an existing photo,
              you will be taken to a classification page and
              presented with our top three guesses of what species
              that plant is. If you know for sure what it
              is, please select one of our three guesses or enter the actual
              common, scientific, or Hawaiian name of the plant.
              If you are not sure, select "I don't know".
            </div>
          </q-timeline-entry>
        </q-timeline>
      </q-card-main>

      <q-card-separator />

      <q-card-actions
        align="center"
      >
        <div class="actions">
          <CameraButton
            v-bind:button="{ color: 'primary' }"
            text="I'm ready to detect plants"
          />
        </div>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
import CameraButton from '../PlantIdentification/CameraButton';

export default {
  name: 'Stepper',
  components: {
    CameraButton,
  },
};
</script>

<style>
.actions {
  margin: 16px;
}
</style>
