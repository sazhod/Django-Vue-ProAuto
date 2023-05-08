<template>
    <div v-for="service in services" class="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-main">{{ service['title'] }}</h5>
        </a>
        <p class="mb-3 font-normal text-text">{{ service['description'] }}</p>
        <p class="mb-3 font-normal text-text">От {{ service['min_price'] }} руб.</p>
        <button type="button" v-bind:data-modal-target="'modal_'+service['id']" v-bind:data-modal-toggle="'modal_'+service['id']" class="inline-flex items-center p-2 rounded-lg font-medium rounded-lg text-sm text-main border border-main hover:bg-main hover:text-dark-text focus:bg-main focus:text-dark-text">
            Примеры работ
            <svg aria-hidden="true" class="w-4 h-4 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
        </button>
        <!-- Main modal -->


            <div tabindex="-1" aria-hidden="true" v-bind:id="'modal_'+service['id']" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
                <div class="relative w-full max-w-2xl max-h-full">
                    <!-- Modal content -->
                    <div class="relative rounded-lg shadow bg-gray-700">
                        <!-- Modal header -->
                        <div class="flex items-start justify-between p-4 border-b rounded-t border-gray-600">
                            <h3  class="text-xl font-semibold text-main">
                                <div v-for="work_example in service['work_examples']">
                                    {{ work_example['description'] }} 
                                </div>
                            </h3>

                            <button type="button" class="text-main bg-transparent hover:bg-main hover:text-dark-text rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" v-bind:data-modal-hide="'modal_'+service['id']">
                                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                                <span class="sr-only">Close modal</span>
                            </button>
                        </div>
                        <!-- Modal body -->
                        <div class="p-6 space-y-6" v-for="work_example in service['work_examples']">
                            <p class="text-base leading-relaxed text-text">
                                Дана начала работы: {{ work_example['start_date'] }}
                            </p>
                            <p class="text-base leading-relaxed text-text">
                                Дана окончания работы: {{ work_example['end_date'] }}
                            </p>
                            <div class="p-4 space-x-1 border-t border-gray-500" v-for="image in work_example['images']">
                                <p class="text-base p-2  leading-relaxed text-text">
                                    Авто: {{ image['title'] }}
                                </p>
                                <div class="grid grid-cols-2 gap-2">
                                    <div>
                                        <img class="h-auto max-w-full rounded-lg" v-bind:src="image['before_image']" alt="">
                                    </div>
                                    <div>
                                        <img class="h-auto max-w-full rounded-lg" v-bind:src="image['after_image']" alt="">
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                        <!-- Modal footer -->
                        <div class="flex items-center p-6 space-x-2 border-t border-gray-500 rounded-b">
                            <button v-bind:data-modal-hide="'modal_'+service['id']" type="button" class="text-main border border-main hover:bg-main hover:text-dark-text font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                                Связаться с нами
                            </button>
                        </div>
                    </div>
                </div>
            </div>

    </div>

</template>

<script>
    import { Service } from '../api/services'
    export default {
        data() {
            return {
                services: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    this.services = await Service.list();
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