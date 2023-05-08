<template>
    {{ images[0]['before_image'] }}
    <img v-bind:src="images[0]['before_image']">
</template>

<script>
    import { Images } from '../api/images'
    export default {
        data() {
            return {
                images: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    this.images = await Images.list();
                } catch (error) {
                    console.log(error);
                }
            },
        },
        created() {
            this.getData();
        }
    }
</script>
