<template>
  <q-card-main>
    <q-table
      grid
      hide-header
      :data="tableData"
      :columns="columns"
      :filter="filter"
      :selection="selection"
      :selected.sync="selected"
      :visible-columns="visibleColumns"
      row-key="name"
    >
      <template slot="top-right" slot-scope="props">
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
            {{ props.row.name }}
          </q-card-title>

          <q-card-separator />

          <q-card-media>
            <img :src="props.row.image" />
          </q-card-media>

          <q-card-actions align=center>
            <q-btn flat>Information <q-icon name="keyboard_arrow_right" /></q-btn>
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
      tableData: [
        {
          name: 'Metrosideros polymorpha',
          image: 'https://www.casaegiardino.it/images/2015/04/20150320_101549-600x450.jpg',
          desc: 'hi',
        },
        {
          name: 'Acacia Koa',
          image: 'https://farm2.staticflickr.com/1366/5187357067_639509a494_o.jpg',
          desc: 'hi',
        },
        {
          name: 'Argemone Glauca',
          image: 'https://www.molokaiseedcompany.com/wp-content/uploads/2017/08/Argemone_glauca_glauca-31-sized.jpg',
          desc: 'hi',
        },
      ],
      columns: [
        {
          name: 'desc',
          required: true,
          label: 'Dessert (100g serving)',
          align: 'left',
          field: 'name',
          sortable: true,
        },
        {
          name: 'calories', label: 'Calories', field: 'calories', sortable: true,
        },
        {
          name: 'fat', label: 'Fat (g)', field: 'fat', sortable: true,
        },
      ],
      filter: '',
      visibleColumns: [
        'desc', 'fat', 'carbs', 'protein', 'sodium', 'calcium', 'iron',
      ],
      separator: 'horizontal',
      selection: 'multiple',
      selected: [
        // initial selection
        {
          name: 'Ice cream sandwich',
        },
      ],
      pagination: {
        page: 2,
      },
      paginationControl: {
        rowsPerPage: 3,
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
};
</script>

<style>

</style>
