

<template>
    <!-- {{ services }} -->
    <div v-if="services[0] === ''">
        Empty
    </div>

    <div v-for="service in services" class="max-w-sm p-6 bg-gray-800 border border-gray-700 rounded-lg shadow">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-main">{{ service.title }}</h5>
        </a>
        <p class="mb-3 font-normal text-text">{{ service.description }}</p>
        <p class="mb-3 font-normal text-text">От {{ service.min_price }} руб.</p>
        <button @click="getWorkExamples(service.id)" type="button" class="inline-flex items-center p-2 rounded-lg font-medium rounded-lg text-sm text-main border border-main hover:bg-main hover:text-dark-text focus:bg-main focus:text-dark-text">
            Примеры работ
            <svg aria-hidden="true" class="w-4 h-4 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
        </button>
    </div>
    <button hidden id="showModal" type="button" data-modal-target="modalWorkExample" data-modal-toggle="modalWorkExample">
        </button>
    <!-- Main modal -->
    <div tabindex="-1" aria-hidden="true" id="modalWorkExample" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
            <div class="relative w-full max-w-2xl max-h-full">
                <!-- Modal content -->
                <div id="modalContent" class="relative rounded-lg shadow bg-gray-700">
                    <!-- Modal header -->
                    <div class="flex items-start justify-between p-4 border-b rounded-t border-gray-600">
                        <h3  class="text-xl font-semibold text-main">
                            Наши работы
                        </h3>
                        <button type="button" class="text-main bg-transparent hover:bg-main hover:text-dark-text rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" data-modal-hide="modalWorkExample">
                            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                            <span class="sr-only">Close modal</span>
                        </button>
                    </div>
                    <!-- Modal body -->
                    <div v-if="showModal">
                        <WorkExample :work_examples="work_examples"/>
                    </div>
                    <!-- Modal footer -->
                    <div class="flex items-center p-6 space-x-2 border-t border-gray-500 rounded-b">
                        <button data-modal-hide="modalWorkExample" type="button" class="text-main border border-main hover:bg-main hover:text-dark-text font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                            Связаться с нами
                        </button>
                    </div>
                </div>
            </div>
        </div>

</template>

<script>
    import { Service } from '../api/services'
    import WorkExample from './WorkExample.vue'
    export default {
        data() {
            return {
                services: [''],
                work_examples: [''],
                showModal: false,
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
            
            async getWorkExamples(service_id){
                try {
                    const responce = await Service.work_examples(service_id);
                    // this.$emit()
                    // document.getElementById('modalContent').innerText = this.work_examples;
                    // document.getElementById("showModal").click()
                    const data = responce.data;
                    this.work_examples = data;
                    console.log(this.work_examples);
                    this.showModal = true;
                    document.getElementById("showModal").click()
                } catch (error) {
                    console.log(error);
                }
            }
        },
        
        mounted() {
            this.getData();
        },
        components: {
            WorkExample
        },
    };
</script>