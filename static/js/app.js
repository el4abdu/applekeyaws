document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const keyDisplay = document.getElementById('key-display');
    const copyBtn = document.getElementById('copy-btn');

    generateBtn.addEventListener('click', () => {
        // Disable button during generation
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';
        keyDisplay.textContent = 'Generating key...';
        keyDisplay.className = 'key-display';

        fetch('/generate_key')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    keyDisplay.textContent = data.key;
                    keyDisplay.classList.add('key-success');
                    copyBtn.style.display = 'inline-block';
                } else {
                    keyDisplay.textContent = 'Key Generation Failed';
                    keyDisplay.classList.add('key-error');
                    copyBtn.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                keyDisplay.textContent = 'An error occurred';
                keyDisplay.classList.add('key-error');
                copyBtn.style.display = 'none';
            })
            .finally(() => {
                // Re-enable button
                generateBtn.disabled = false;
                generateBtn.textContent = 'Generate Key';
            });
    });

    copyBtn.addEventListener('click', () => {
        const key = keyDisplay.textContent;
        navigator.clipboard.writeText(key).then(() => {
            copyBtn.textContent = 'Copied!';
            copyBtn.classList.add('btn-success');
            
            setTimeout(() => {
                copyBtn.textContent = 'Copy Key';
                copyBtn.classList.remove('btn-success');
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy: ', err);
        });
    });
}); 