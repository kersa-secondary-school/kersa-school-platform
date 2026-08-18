containerclasslass Container {
constructorctor(containerId) {
        this.container = document.getElementById(containerId);
        if (!this.container) {
            throw new Error(`Container with ID "${containerId}" not found.`);
        }
    }

    // Method to create and append a new element
    createElement(tag, options = {}) {
        const element = document.createElement(tag);

        // Set attributes if provided
        if (options.attributes) {
            for (const [key, value] of Object.entries(options.attributes)) {
                element.setAttribute(key, value);
            }
        }

        // Set inner content if provided
        if (options.content) {
            element.innerHTML = options.content;
        }

        // Append the element to the container
        this.container.appendChild(element);
        return element;
    }

    // Method to clear the container
    clear() {
        this.container.innerHTML = '';
    }

    // Method to remove an element by its ID
    removeElementById(elementId) {
        const element = document.getElementById(elementId);
        if (element) {
            this.container.removeChild(element);
        } else {
            console.warn(`Element with ID "${elementId}" not found.`);
        }
    }
}

// Example usage:
// Initialize the container with an ID of your choice
const myContainer = new Container('myContainer');

// Create and append elements
myContainer.createElement('h1', { content: 'Welcome to My Container' });
myContainer.createElement('p', { 
    content: 'This is a dynamically created paragraph.',
    attributes: { class: 'dynamic-paragraph' } 
});

// Clear the container
// myContainer.clear();

// Remove an element by ID
// myContainer.removeElementById('someElementId');ly:
