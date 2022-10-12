function Popular() {
  const getPopular = async () => {
    const api = await fetch(
      `https://api.spoonacular.com/recipes/random?apiKey=${pro}`
    );
  };

  return <div>Popular</div>;
}

export default Popular;
