// Cypress End-to-End Tests for UI

describe('LLM Alignment Assistant UI Tests', () => {
    it('Loads the Home Page and Checks Dark Mode Toggle', () => {
      cy.visit('http://localhost:5000');
      cy.get('#dark-mode-toggle').click();
      cy.get('body').should('have.class', 'dark-mode');
      cy.get('#dark-mode-toggle').click();
      cy.get('body').should('not.have.class', 'dark-mode');
    });
  
    it('Submits User Feedback', () => {
      cy.visit('http://localhost:5000/feedback');
      cy.get('#rating').type('5');
      cy.get('#comments').type('The response was very helpful.');
      cy.get('form').submit();
      cy.contains('Thank you for your feedback!');
    });
  });
  