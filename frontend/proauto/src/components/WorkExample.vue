<template>
    <!-- Modal body -->
    <!-- v-for="work_example in work_examples" -->
    <div v-for="work_example in work_examples"  class="space-y-6 p-4 space-x-1 border-t border-gray-500">
        <p  class="text-base leading-relaxed text-text">
            {{ work_example.description }} 
        </p>
        <p class="text-base leading-relaxed text-text">
            Дана начала работы: {{ work_example.start_date }}
            Test
        </p>
        <p class="text-base leading-relaxed text-text">
            Дана окончания работы: {{ work_example.end_date }}
        </p>
        <!-- v-for="image in work_example.images" -->
        <div v-for="image in work_example.images">
            <p class="text-base p-2  leading-relaxed text-text">
            Авто: {{ image.title }}
            </p>
            <div class="grid grid-cols-2 gap-2">
                <div>
                    <img class="h-auto max-w-full rounded-lg" v-bind:src="'http://localhost:8000/'+image.before_image" alt="">
                </div>
                <div>
                    <img class="h-auto max-w-full rounded-lg" v-bind:src="'http://localhost:8000/'+image.after_image" alt="">
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
    export default {
        props: {
            work_examples: Object
        },
    }
</script>