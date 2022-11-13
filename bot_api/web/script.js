/* поле, в которое поступает информация о результатах исполнения логики */
let log = document.querySelector("#log");
/* поле, в которое можно вписать искомый объект */
let objName = document.querySelector("#object_name");
/* кнопка "Получить id объекта */
let getObjectsInfoBtn = document.querySelector("#get_objects_info_btn");
/* кнопка "Получить id объекта */
let saveObjectsInfoBtn = document.querySelector("#save_objects_info_btn");

/* закидываем информацию в лог из питона */
async function getObjectInfo() {
    log.value = await eel.get_objects_info(objName.value)();
}
async function saveObjectInfo() {
    log.value = await eel.save_objects_cords(objName.value)();
}

        // async function getObjectCordsCycle() {
        //     while (cycleCbx.checked) {
        //         log.value = await eel.get_cycle_data(objName.value)();
        //     }
        // }


/* отлавливаем клик на нашу кнопку и вызываем функцию */
getObjectsInfoBtn.addEventListener("click", () => {
    getObjectInfo();
})

/* отлавливаем клик на нашу кнопку и вызываем функцию */
saveObjectsInfoBtn.addEventListener("click", () => {
    saveObjectInfo();
})