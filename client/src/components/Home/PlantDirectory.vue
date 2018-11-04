<template>
  <q-card>
    <q-card-title>Browse the flora of Hawaii</q-card-title>
    <q-card-separator />
    <q-card-main>
      <q-table
        grid
        :pagination.sync="serverPagination"
        :data="tableData"
        :columns="columns"
        :filter="filter"
        :loading="loading"
        row-key="plant_name"
        @request="request"
      >
        <template slot="top" slot-scope="props">
          <q-search
            hide-underline
            clearable
            v-model="filter"
          />
        </template>

        <div
          slot="item"
          slot-scope="props"
          class="q-pa-xs col-xs-12 col-sm-6 col-md-4 transition-generic"
          :style="props.selected ? 'transform: scale(0.95);' : ''"
        >
          <q-card
            class="transition-generic"
            :class="props.selected ? 'bg-grey-2' : ''"
            @click.native="props.selected = !props.selected"
          >
            <q-card-title
              class="relative-position"
            >
              {{ props.row.plant_name }}
            </q-card-title>

            <q-card-separator />

            <q-card-media>
              <img
                :src="props.row.image"
              />
            </q-card-media>

            <q-card-actions align="center">
              <q-btn
                flat
                :to="`/plant/${props.row.id}`"
              >
                Information
                <q-icon
                  name="keyboard_arrow_right"
                />
              </q-btn>
            </q-card-actions>
          </q-card>
        </div>
      </q-table>
    </q-card-main>
  </q-card>
</template>

<script>
export default {
  data() {
    return {
      serverPagination: {
        page: 1,
        rowsNumber: 9,
        rowsPerPage: 9,
      },
      tableData: [],
      columns: [],
      filter: '',
      separator: 'horizontal',
      selection: 'multiple',
      selected: [],
      loading: true,
      dark: true,
    };
  },
  methods: {
    request({ pagination }) {
      // we set QTable to "loading" state
      this.loading = true;

      // we do the server data fetch, based on pagination and filter received
      // (using Axios here, but can be anything; parameters vary based on backend implementation)

      this.$axios
        .get(`http://localhost:3000/api/plants/${pagination.rowsPerPage}/${(pagination.page - 1) * pagination.rowsPerPage}`)
        .then(({ data }) => {
          // updating pagination to reflect in the UI
          this.serverPagination = pagination;

          // then we update the rows with the fetched ones
          this.tableData = data;

          // finally we tell QTable to exit the "loading" state
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },
  },
  mounted() {
    // once mounted, we need to trigger the initial server data fetch
    this.$axios
      .get('http://localhost:3000/api/count/plant')
      .then((response) => {
        const { data } = response;

        // specify the number of rows in total
        this.serverPagination.rowsNumber = data.count;
      })
      .then(() => {
        // invoke request method to get initial data

        this.request({
          pagination: this.serverPagination,
          filter: this.filter,
        });

        // finish loading
        this.loading = false;
      })
      .catch((err) => {
        console.log(err);
        this.loading = false;
      });
  },
};
</script>

<style>

</style>
