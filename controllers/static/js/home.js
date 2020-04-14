window.onload = function () {
    $.getJSON("/api/recipes", function(data) {
        $.each(data, function(key, val) {
            let li = $("<li>")
            li.attr("recette", val.id).attr("source", val.id_src)
            li.append($("<a>").attr("href","/recette/"+val.id).html(val.name))
            $("#listRecipes").append(li)
            $.getJSON("/api/categories/recipe/" + val.id, function(data) {
                $.each(data, function(key, val) {
                    li.append($("<div>").attr("hidden", "hidden").attr("category", val.id))
                })
            })
            $.getJSON("/api/ingredients/recipe/" + val.id, function(data) {
                $.each(data, function(key, val) {
                    li.append($("<div>").attr("hidden", "hidden").attr("ingredient", val.id_ingredient))
                })
            })
        })
    })
    $.getJSON("/api/sources", function(data) {
        $.each(data, function(key, val) {
            $("#sources").append($("<option>").val(val.id).html(val.name))
        })
    })
    $.getJSON("/api/categories", function(data) {
        $.each(data, function(key, val) {
            let label = $("<label>").attr("for", "category"+val.id).html(val.name)
            let input = $("<input>").addClass("category")
                                    .attr("id", "category"+val.id)
                                    .attr("type", "checkbox").val(val.id)
                                    .attr("onclick", "filter_all()")
                                    .html(val.name)
            $("#categories").append(label).append(input)
        })
    })
    $.getJSON("/api/ingredients", function(data) {
        $.each(data, function(key, val) {
            let label = $("<label>").attr("for", "ingredient" + val.id).html(val.name)
            let input = $("<input>").addClass("ingredient")
                                    .attr("id", "ingredient" + val.id)
                                    .attr("id", "ingredient"+val.id)
                                    .attr("type", "checkbox").val(val.id)
                                    .attr("onclick", "filter_all()")
                                    .html(val.name)
            let li = $("<li>").append(input).append(label).addClass("li_ingredient")
            $("#listIngredients").append(li)
        })
    })
}

$("#hamburger").click(function () {
    $("#links").toggle()
})

$("#buttonIngredients").click(function () {
    $("#ingredients").toggle()
})

let filter_all = function(){
    let tag = $("#searchRecipeByName").val().toLowerCase()
    let source = $("#sources").val()
    let checked = []
    let ingredients_checked = []
    $("input.category").each(function () {
        if ($(this).is(':checked')){
            checked.push(parseInt($(this).val()))
        }
    })
    $("input.ingredient").each(function () {
        if ($(this).is(':checked')){
            ingredients_checked.push(parseInt($(this).val()))
        }
    })

    let recipes = $("li[recette]")
    recipes.each(function () {
        $(this).hide()
    })
    let filtered_recipes = []
    recipes.each(function () {
        if ($(this).text().toLowerCase().indexOf(tag) > -1){
            filtered_recipes.push($(this))
        }
    })

    recipes = filtered_recipes
    filtered_recipes = []

    if (source != null && source !=0){
        recipes.forEach(function (elem) {
            if (elem.attr("source").toLowerCase().indexOf($("#sources").val()) > -1){
                filtered_recipes.push(elem)
            }
        })
        recipes = filtered_recipes
        filtered_recipes = []
    }

    if (checked.length != 0) {
        recipes.forEach(function (recipe) {
            let categories = []
            recipe.find("div[category]").each(function(){
                categories.push(parseInt($(this).attr("category")))
            })
            categories.forEach(function (elem) {
                if(checked.indexOf(elem) > -1 && filtered_recipes.indexOf(recipe) == -1){
                    filtered_recipes.push(recipe)
                }
            })
        })
        recipes = filtered_recipes
        filtered_recipes = []
    }

    if (ingredients_checked.length != 0){
        recipes.forEach(function (recipe) {
            let ingredients = []
            let display = true
            recipe.find("div[ingredient]").each(function () {
                ingredients.push(parseInt($(this).attr("ingredient")))
            })
            ingredients_checked.forEach(function (elem) {
                if(ingredients.indexOf(elem) == -1) {
                    display = false
                }
            })
            if (display && filtered_recipes.indexOf(recipe) == -1){
                filtered_recipes.push(recipe)
            }
        })
        recipes = filtered_recipes
        filtered_recipes = []
    }

    recipes.forEach(function (recipe) {
        recipe.show()
    })
}

$("#searchRecipeByName").keyup(function () {
  filter_all()
})
 $("#sources").change(function () {
  filter_all()
 })