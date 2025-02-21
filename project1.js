document.addEventListener('DOMContentLoaded', () => {
    const recipes = [
        {
            title: "Spaghetti Bolognese",
            description: "A classic Italian pasta dish.",
            ingredients: ["spaghetti", "eggs", "parmesan cheese", "pancetta", "pepper"],
            steps: [
                "Boil the spaghetti", 
                "Cook the pancetta until crisp ", 
                "Mix eggs and cheese in a bowl", 
                "combine spaghetti with pancetta and remove from heat",
                "Stir in the egg mixture and serve"
            ],
            image: "spaghetti_carbonara.jpg"
        },
        {
            title: "chicken curry",
            description: "A flavorful chicken curry",
            ingredients: ["Chicken", "Onions", "Tomatoes", "Garlic", "spices"],
            steps: [
            "Saute onions and garlic", 
            "Add spices and cook until fragrant ", 
            "Add chicken and brown", 
            "Add tomatoes and simer until chicken is cooked",
            "Serve with rice"
            ],
            image: "chicken_curry.jpg"
        },
        {
            title: " Grilled Chicken with Lemon and Herbs",
            description: "delicious Grilled Chicken with Lemon and Herbs!",
            ingredients: ["Chicken breasts", "olive oil", "1 lemon", "Garlic", "spices"],
            steps: [
            "Olive oil, lemon juice, garlic, and spices should all be mixed in a shallow dish. After adding, change the chicken breasts to ensure they are even coating. Put the cover on and let it marinate in the fridge for half an hour or more.", 
            "Preheat grill to medium-high heat ", 
            "Grill the chicken for 5-7 minutes per side, or until cooked through and no longer pink in the center. The internal temperature should reach 165°F (74°C).",
            "Serve the grilled chicken immediately, garnished with any remaining lemon slices or fresh herbs if desired."
            ],
            image: "grilled with lemon.jpg" 
        },
        // Add more recipe objects here
    ];

    const searchButton = document.getElementById('search-button');
    const searchBar = document.getElementById('search-bar');
    const recipeList = document.getElementById('recipe-list');
    const recipeDetails = document.getElementById('recipe-details');

    searchButton.addEventListener('click', () => {
        const query = searchBar.value.toLowerCase();
        const filteredRecipes = recipes.filter(recipe => recipe.title.toLowerCase().includes(query));
        displayRecipeList(filteredRecipes);
    });

    const displayRecipeList = (recipes) => {
        recipeList.innerHTML = '';
        recipes.forEach(recipe => {
            const recipeDiv = document.createElement('div');
            recipeDiv.classList.add('recipe');
            recipeDiv.textContent = `${recipe.title}: ${recipe.description}`;
            recipeDiv.addEventListener('click', () => displayRecipeDetails(recipe));
            recipeList.appendChild(recipeDiv);
        });
    };

    const displayRecipeDetails = (recipe) => {
        recipeDetails.innerHTML = `
            <h2>${recipe.title}</h2>
            <img src="${recipe.image}" alt="${recipe.title}">
            <h3>Ingredients</h3>
            <ul>
                ${recipe.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
            </ul>
            <h3>Steps</h3>
            <ol>
                ${recipe.steps.map(step => `<li>${step}</li>`).join('')}
            </ol>
            <button id="print-button">Print Recipe</button>
        `;

        const ingredientItems = recipeDetails.querySelectorAll('li');
        ingredientItems.forEach(item => {
            item.addEventListener('click', () => {
                item.classList.toggle('purchased');
            });
        });

        const printButton = document.getElementById('print-button');
        printButton.addEventListener('click', () => {
            window.print();
        });
    };
});