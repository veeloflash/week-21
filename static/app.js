document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('search-form');
  const algorithmSelect = document.getElementById('algorithm');
  const algorithmHint = document.getElementById('algorithm-hint');
  if (form && algorithmSelect && algorithmHint) {
    algorithmSelect.addEventListener('change', () => {
      const value = algorithmSelect.value;
      if (value === 'tfidf') algorithmHint.textContent = 'TF-IDF uses lexical overlap and term weighting.';
      else if (value === 'cosine') algorithmHint.textContent = 'Cosine similarity compares vector direction.';
      else if (value === 'euclidean') algorithmHint.textContent = 'Euclidean distance compares geometric distance.';
      else algorithmHint.textContent = 'Embedding search uses semantic representation.';
    });
  }
});
