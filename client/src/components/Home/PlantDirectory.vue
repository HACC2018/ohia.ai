<template>
  <q-card-main>
    <q-table
      grid
      hide-header
      :pagination.sync="serverPagination"
      :data="tableData"
      :columns="columns"
      :filter="filter"
      :selection="selection"
      :selected.sync="selected"
      :visible-columns="visibleColumns"
      :loading="loading"
      row-key="plant_name"
      @request="request"
    >
      <template slot="top" slot-scope="props">
        <q-search hide-underline clearable v-model="filter" />
      </template>

      <div
        slot="item"
        slot-scope="props"
        class="q-pa-xs col-xs-12 col-sm-6 col-md-4 transition-generic"
        :style="props.selected ? 'transform: scale(0.95);' : ''"
      >
        <q-card
          class="transition-generic cursor-pointer"
          :class="props.selected ? 'bg-grey-2' : ''"
          @click.native="props.selected = !props.selected"
        >
          <q-card-title class="relative-position">
            {{ props.row.plant_name }}
          </q-card-title>

          <q-card-separator />

          <q-card-media>
            <img :src="props.row.image" />
          </q-card-media>

          <q-card-actions align="center">
            <q-btn flat :to="`/plant/${props.row.id}`">
              Information
              <q-icon name="keyboard_arrow_right" />
            </q-btn>
          </q-card-actions>
        </q-card>
      </div>
    </q-table>
  </q-card-main>
</template>

<script>
export default {
  data() {
    return {
      serverPagination: {
        page: 1,
        rowsNumber: 10,
        rowsPerPage: 9,
      },
      tableData: [],
      columns: [
        {
          name: 'desc',
          required: true,
          label: 'Dessert (100g serving)',
          align: 'left',
          field: 'name',
          sortable: true,
        },
      ],
      filter: '',
      separator: 'horizontal',
      selection: 'multiple',
      selected: [
        // initial selection
        {
          name: '',
        },
      ],
      pagination: {
        page: 2,
      },
      paginationControl: {
        rowsPerPage: 9,
        page: 1,
      },
      loading: false,
      dark: true,
      selectedSecond: [
        {
          name: 'Eclair',
        },
      ],
    };
  },
  methods: {
    request({ pagination }) {
      // we set QTable to "loading" state
      this.loading = true;

      // we do the server data fetch, based on pagination and filter received
      // (using Axios here, but can be anything; parameters vary based on backend implementation)

      console.log(pagination);

      this.$axios
        .get(`http://localhost:3000/api/plants/100/${(pagination.page - 1) * 9}`)
        .then(({ data }) => {
          // updating pagination to reflect in the UI
          this.serverPagination = pagination;

          // we also set (or update) rowsNumber
          this.serverPagination.rowsNumber = data.rowsNumber;

          // then we update the rows with the fetched ones
          this.tableData = data;

          // finally we tell QTable to exit the "loading" state
          this.loading = false;
        })
        .catch(() => {
          // there's an error... do SOMETHING

          // we tell QTable to exit the "loading" state
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

        console.log(this.serverPagination.rowsNumber);
        this.serverPagination.rowsNumber = data.count;
      });

    this.request({
      pagination: this.serverPagination,
      filter: this.filter,
    });
  },
};
</script>

<style>

</style>
