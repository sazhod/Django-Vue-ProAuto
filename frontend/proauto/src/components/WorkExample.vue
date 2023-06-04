<template>
    <!-- Modal body -->
    <!-- v-for="work_example in work_examples" -->
    <div v-for="work_example in work_examples.work_examples"  class="space-y-2 p-4 border-t border-menu-border m-2">
        <p class="md:text-desktop-card-body text-mobile-card-body text-base leading-relaxed text-text">
            {{ work_example.description }} 
        </p>
        <p v-if="work_example.start_date" class="md:text-desktop-card-body text-mobile-card-body text-base text-text">
            Дана начала работы: {{ work_example.start_date }}
        </p>
        <p v-if="work_example.end_date" class="md:text-desktop-card-body text-mobile-card-body text-base leading-relaxed text-text">
            Дана окончания работы: {{ work_example.end_date }}
        </p>
        <!-- v-for="image in work_example.images" -->
        <div v-for="image in work_example.images">
            <p class="md:text-desktop-card-body text-mobile-card-body text-base mb-2 leading-relaxed text-text">
            Авто: {{ image.title }}
            </p>
            <div class="grid grid-cols-2 gap-2">
                <div>
                    <a v-bind:href="'http://localhost:8000/'+image.before_image">
                        <img class="h-auto max-w-full rounded-lg" v-bind:src="'http://localhost:8000/'+image.before_image" alt="До">
                    </a>
                </div>
                <div>
                    <img class="h-auto max-w-full rounded-lg" v-bind:src="'http://localhost:8000/'+image.after_image" alt="После">
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
    export default {
        props: {
            work_examples: Object,
        },
    }
</script>