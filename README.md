# Updated and Detailed Overview of the Task

The task involves designing a comprehensive Natural Language Processing (NLP) tokenizer named MNLPTK (Minimal Natural Language Processing Tokenizer) to analyze and evaluate speech interactions, specifically telephone calls in Spanish. This project aims to assess two primary aspects of these interactions:

1. **Employee Performance**: Evaluate if the employee performed according to established criteria.
2. **Customer Experience**: Assess the overall satisfaction and experience of the customer during the call.

## Enhanced Features of the Tokenizer

To improve the functionality and accuracy of the tokenizer, we will incorporate advanced NLP techniques and strategies:

- **Emotional Tone Detection**
- **Stop Words Removal**
- **Contextual Understanding**
- **Co-reference Resolution**
- **Dialogue Act Recognition**
- **Robustness and Error Handling**
  - Error Detection and Correction
  - Fallback Strategies
- **Visual Analytics**
  - Graphs
  - Charts
  - Heatmaps

## Design and Conceptual Steps

### 1. Understanding the Objectives and Requirements

**Primary Objectives:**

- **Identify and classify words (lexemes) in the input text**: This involves breaking down the conversation into smaller, meaningful units called tokens.
- **Evaluate interactions based on identified tokens and emotional tone**: This step involves analyzing the tokens to assess the employee's performance and the customer's experience.
- **Generate scores for employee performance and customer experience**: Numerical scores will be assigned based on predefined criteria to quantify the evaluation.
- **Handle various types of words and expressions**: The tokenizer must be able to recognize and process greetings, farewells, positive/negative words, and other significant expressions.

**Additional Requirements:**

- **Provide insights into the emotional tone of the conversation**: Understanding the emotions expressed during the interaction can provide deeper insights into customer satisfaction.
- **Remove common stop words to focus on meaningful content**: Stop words (e.g., "the", "is", "at") are commonly removed to focus on the significant words in the text.
- **Understand contextual references to handle pronouns and ensure accurate tokenization**: Co-reference resolution is necessary to track pronouns and references back to the appropriate nouns.
- **Recognize dialogue acts to understand the purpose of each utterance**: Dialogue acts (e.g., question, request, apology) help in understanding the structure and flow of the conversation.

### 2. Input and Output

**Input:**

- Two text files: One containing the employee's dialogue and the other containing the customer's dialogue.

**Output:**

- **Evaluation score for employee performance**: A numerical score representing the employee's adherence to performance criteria.
- **Evaluation score for customer experience**: A numerical score reflecting the overall customer satisfaction.
- **List of tokens justifying the scores**: Detailed tokens identified in the conversation that justify the scores.
- **Emotional tone analysis of the conversation**: Analysis of the emotional content of the conversation.
- **Visual analytics in the form of graphs, charts, and heatmaps**: Visual representations of the analysis results.

### 3. Detailed Design Steps

#### Step 1: Reading Input Files

**Description**: Read and parse the transcript files separately for employee and customer dialogues.  
**Purpose**: To prepare the raw data for further processing and analysis.

#### Step 2: Token Definition

**Description**: Define a comprehensive set of tokens that will be used to evaluate the dialogue.

**Examples**:
- Greetings: "buenos días", "buenas tardes"
- Farewells: "hasta luego", "adiós"
- Positive words: "bueno", "excelente"
- Negative words: "mal", "desastre"

**Purpose**: To identify specific words or phrases that are important for evaluating the interaction.

#### Step 3: Emotional Tone Detection

**Description**: Use an emotion detection model or library to classify the emotional tone of the conversation.  
**Purpose**: To gain insights into the emotional states of both the employee and the customer during the interaction.

#### Step 4: Stop Words Removal

**Description**: Remove common stop words that do not contribute to the sentiment or meaning of the conversation.  
**Purpose**: To focus on the significant words and reduce noise in the data.

#### Step 5: Contextual Understanding

**Co-reference Resolution**:  
**Description**: Implement techniques to resolve pronouns and references.  
**Purpose**: To ensure the tokenizer understands what each pronoun refers to, improving accuracy.

**Dialogue Act Recognition**:  
**Description**: Identify the purpose of each utterance (e.g., question, request, apology).  
**Purpose**: To understand the dialogue structure better and provide context to the interaction.

#### Step 6: Error Detection and Correction

**Description**: Implement mechanisms to detect and correct common errors in transcripts, such as spelling mistakes or transcription errors.  
**Purpose**: To improve the accuracy and reliability of the tokenization process.

#### Step 7: Fallback Strategies

**Description**: Develop fallback strategies for handling unknown tokens or unexpected input.  
**Purpose**: To ensure the system remains robust and reliable under various conditions.

#### Step 8: Lexical Analysis

**Description**: Use techniques such as finite automata or regular expressions to identify and classify tokens in the text.  
**Purpose**: To systematically break down the text into meaningful tokens.

#### Step 9: Scoring Mechanism

**Description**: Assign scores based on identified tokens and emotional tone using predefined rules.  
**Purpose**: To provide quantitative evaluations of employee performance and customer experience.

#### Step 10: Visual Analytics

**Description**: Write the tokenization and scoring data to an Excel file. Create visualizations in Excel to display emotional tone, dialogue flow, and scoring trends.  
**Purpose**: To provide a clear and accessible representation of the analysis results.

#### Step 11: Post-Processing

**Description**: Allow for manual adjustments of neutral words to classify them as positive or negative. Update token patterns based on user inputs and feedback.  
**Purpose**: To continuously improve the system based on new data and user feedback.

## Example Workflow

**Read Input Files**:
- Load the employee and customer transcripts into the system.

**Tokenization and Preprocessing**:
- Remove stop words: Filter out common stop words to focus on meaningful content.
- Correct spelling errors: Use a spell checker to correct any spelling mistakes in the text.
- Resolve co-references: Implement co-reference resolution to accurately link pronouns to their respective nouns.

**Token Identification**:
- Match the text against predefined token patterns to identify significant words and phrases.

**Emotion and Dialogue Act Analysis**:
- Analyze the emotional tone of the conversation to understand the emotional states of the participants.
- Recognize dialogue acts to determine the purpose of each utterance (e.g., whether it is a question or a statement).

**Scoring**:
- Calculate scores based on the identified tokens and emotional analysis.
- Aggregate the scores to provide an overall evaluation of employee performance and customer experience.

**Visual Analytics**:
- Write the processed data (tokens, scores, emotions, dialogue flow) to an Excel file with separate sheets for each type of data.
- Create visualizations (graphs, charts, heatmaps) in Excel to display the analysis results.

**Post-Processing and Feedback**:
- Allow users to manually adjust the classification of neutral words.
- Update token patterns and scoring rules based on new data and user feedback to continuously improve the system.

## Conclusion

This detailed design outlines a comprehensive approach to developing a robust and insightful NLP tokenizer for evaluating telephone interactions. By incorporating advanced NLP techniques and visual analytics, the tokenizer will provide valuable insights into both employee performance and customer experience, ensuring a thorough and accurate analysis of the interactions. This approach also emphasizes the importance of user feedback and continuous improvement to keep the system effective and relevant.

# Trabajo Práctico Diseño de Compiladores: Tokenizador NLP

## Motivación

Las herramientas de procesamiento de lenguajes naturales (NPL) se aplican sobre lenguajes naturales y deben manejar diversas situaciones como ambigüedades, expresiones literarias, o modismos regionales. El analizador léxico necesita herramientas específicas como preprocesadores léxicos para identificar palabras. Los tokenizadores ayudan a identificar y organizar palabras, simplificando el análisis sintáctico posterior.

## Objetivo del Trabajo Práctico

Construir un tokenizador mínimo, MNLPTK (Minimal Natural Language Processing Tokenizer), que actúe como solución de análisis de conversaciones telefónicas en español. Procesará las palabras (lexemas) identificadas para evaluar dos aspectos principales:

- **Desempeño del Funcionario**: Evaluar si el funcionario se desempeñó según criterios establecidos.
- **Evaluación de la Llamada**: Evaluar la experiencia del cliente, considerando si se resolvió su necesidad.

Estos indicadores permiten tomar acciones para fidelizar al cliente, como capacitar al funcionario en caso de bajo desempeño o seguir la experiencia negativa con acciones comerciales.

## Descripción del Alcance

Los tokens definidos deben permitir evaluar la atención y la experiencia del cliente. Algunos ejemplos de tokens son:

- **Experiencia del Cliente**: EXP_MALA, EXP_NEUTRA, EXP_BUENA
- **Atención del Funcionario**: ATC_MALA, ATC_NEUTRA, ATC_BUENA

La llamada se transcribe en dos archivos, uno para la interacción del personal de atención al cliente y otro para la interacción del cliente. Esto permite dividir el tokenizador en dos procesos especializados para la evaluación.

El programa comienza leyendo el archivo del funcionario, obteniendo una evaluación de la gestión según los patrones definidos, y luego el archivo del cliente, evaluando su experiencia.

## Criterios de Evaluación

- **Experiencia de Atención**: Identificar saludos ("buenos días", "buenas tardes", "buenas noches") y despedidas ("hasta luego"). Identificar al cliente con palabras como "documento" o "cédula", y cortesías como "gracias" y "por favor".
- **Experiencia del Cliente**: Identificar palabras negativas (e.g., "mal", "desastre", "cansado") y positivas (antónimos de las negativas) para generar una evaluación en una escala del 1 al 5.

Para palabras neutras, se puede ajustar manualmente su clasificación como positivas o negativas, actualizando los patrones de tokens.

Al finalizar el análisis léxico, se obtendrá:

- Una ponderación para la experiencia de atención y otra para la del cliente.
- El detalle de cómo se llegó a esas ponderaciones.
- La posibilidad de recorrer y asignar manualmente palabras neutras como positivas o negativas.

## Mejoras

1. **Número y Género**: Considerar variantes de género y número para palabras buenas o malas (e.g., "mal", "malo", "mala", "malos", "malas").
2. **Interfaz Gráfica Amigable**.

## Metodología

Utilizar conocimientos de clases para construir el tokenizador, pudiendo emplear:

1. **Algoritmo de Simulación de AFD**: Para obtener lexemas a partir de patrones definidos por expresiones regulares.
2. **Herramientas de IA**: Como soporte y ayuda (e.g., ChatGPT), pero la responsabilidad de la codificación y ejecución es del alumno. Se deben identificar y corregir conocimientos inexactos de estas herramientas.

El lenguaje de programación es libre elección del alumno.

## Entregables y Defensa del Trabajo Práctico

Entregables:

1. Documento en PDF describiendo:
   - El trabajo práctico.
   - Decisiones adoptadas.
   - Mejoras.
   - Estrategias aplicadas.
2. Código fuente.
3. Resultado para un caso de ejemplo.
4. Observaciones sobre el funcionamiento.

La defensa del trabajo práctico es presencial, no recuperable, y requisito para rendir el examen final. Se debe presentar:

- Funcionalidades y ejemplos.
- Evaluación de eficiencia, funcionamiento y validaciones.

## Evaluación

La evaluación consta de:

- **Parte Práctica**: Defensa del trabajo práctico, evaluando funcionalidades, ejemplos y validaciones.
- **Parte Teórica**: Evaluación del documento PDF y el algoritmo implementado.

## Observaciones

- **No recuperable**.
- **Fecha de entrega**: Último lunes de clases antes del segundo parcial.
- **Trabajo individual**.
- **Máximo 15 minutos para la defensa**.
