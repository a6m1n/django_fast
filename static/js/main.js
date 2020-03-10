$(document).ready(function() {
    $('div.input-group input[type=checkbox]').hide();

    $("#list-languages").on("click", "span.my-remove", function(event){
        event.preventDefault();
        let block = this.parentNode;
        let checkbox = block.querySelectorAll('input[type=checkbox]')[0];
        checkbox.checked = true;
        block.style.display = "none";
    });

    function get_new_id(tree) {
        //GET NUMBER ID
        let div = tree.querySelector('div:last-child');
        if (!div){
            return 0;
        }

        let id = div.firstElementChild.id;

        let arrayOfStrings = id.split('-');
        let index = arrayOfStrings[1];

        let new_id =  Number(index)+1;
        if (isNaN(new_id)){
            return 0;
        }
        return new_id;
    }

    $('#create-block').click(function(event) {
        event.preventDefault();
        let value_in_field_lang = $('#main-lang select')[0].value;

        if (value_in_field_lang !== ''){
            let block = document.getElementById('list-languages');
            let id = get_new_id(block);
            let to_copy = block.lastElementChild;
            let new_block = document.createElement('div');
            new_block.className = 'input-group';
            new_block.innerHTML = to_copy.innerHTML;
            update_id(new_block, id);
            up_total_forms();

            block.append(new_block);
            set_value(new_block, value_in_field_lang);
            set_default_value_to_main_select();
        }

    });

    function update_id(block, id) {
        for(let i=0; i<block.childNodes.length; i++) {
            let elem = block.childNodes[i];
            if (elem.nodeName.toLowerCase()!=='#text'){
                up_attr(elem);
            }
        }
    }

    function up_attr(element) {
       if (element.id){
            element.id = set_new_attr(element.id);
        }
        if (element.name){
            element.name = set_new_attr(element.name);
        }
    }

    function set_new_attr(str_obj) {
        let arrayOfStrings = str_obj.split('-');
        let index = arrayOfStrings[1];
        let new_id =  Number(index)+1;
        return `${arrayOfStrings[0]}-${new_id}-${arrayOfStrings[2]}`;

    }

    function up_total_forms() {
        let elem = document.getElementById('id_leadlanguages_set-TOTAL_FORMS');
        elem.value = Number(elem.value) + 1;
    }

    function set_value(block, value) {
        let select = block.getElementsByTagName('select')[0];
        select.value = value;
    }
    function set_default_value_to_main_select() {
        $('#main-lang select')[0].value = 0;
    }

});
