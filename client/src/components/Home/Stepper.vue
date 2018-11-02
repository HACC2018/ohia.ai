<template>
  <div>
    <q-card>
      <q-card-title>
        Locating and identifying native and invasive plant species
      </q-card-title>

      <q-card-separator />

      <q-card-main>
        <q-timeline responsive color="secondary">
          <q-timeline-entry
            title="Allow us to use your camera."
            side="right"
            subtitle="Step 1"
            icon="camera"
          >
            <div>
              To begin helping us identify plant species
              in Hawaii, begin by allowing this application
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
              In addition, we request that you allow us to view your
              location to locate where the plant is located. When you
              take the picture, your GPS location will be recorded to
              help the State of Hawaii protect and track native plants and
              possibly eradicate invasive plants.
            </div>
          </q-timeline-entry>

          <q-timeline-entry
            title="Snap the image."
            side="right"
            subtitle="Step 3"
            icon="camera_alt"
          >
            <div>
              While taking the image of the plant, keep in mind:
              take photos that are close, in focus and well lit.
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
              After taking the image, you will be taken to a classification
              page and presented with our top three guesses of what species
              that plant you took a picture is. If you know for sure what it
              is, please select one of our selected guesses or enter the actual
              genus of the plant. If you are not sure, select "I don't know".
            </div>
          </q-timeline-entry>
        </q-timeline>
      </q-card-main>

      <q-card-separator />

      <q-card-actions>
        <div class="actions">
          <q-btn color="primary" to="/detector">I'm ready to detect plants</q-btn>
        </div>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'Stepper',
};
</script>

<style>
.actions {
  margin: 16px;
}
</style>
