
const app = Vue.createApp({
    data() {
        return {
            pokemon: [],
            pokemon_search: "",
            showDropdown: false,
        }
    },
    methods: {

    },
    computed: {
        filteredPokemon() {
            if (this.pokemon_search.length < 1) return this.pokemon
            return this.pokemon.filter(pokemon => {
                return pokemon.name.toLowerCase().includes(this.pokemon_search.toLowerCase())
            })
        }
    },
    async created() {
        const res = await fetch('/api/pokemon')
        const pokemon = await res.json()
        this.pokemon = pokemon.pokemon
    }
})

app.config.compilerOptions.delimiters = ['[[', ']]']
app.mount('#app')