import streamlit as st
import json
import os
import random

# Page Configuration
st.set_page_config(
    page_title="AI Learning Hub",
    page_icon="🤖",
    layout="wide"
)

# Topic Configuration
topic_files = {
    "AI": "data/ai.json",
    "Generative AI": "data/generative_ai.json",
    "Agentic AI": "data/agentic_ai.json",
    "Prompt Engineering": "data/prompt_engineering.json",
    "Machine Learning": "data/machine_learning.json",
    "Deep Learning": "data/deep_learning.json",
    "Different AI Apps": "data/ai apps.json"
}

# Quiz Configuration
quiz_files = {
    "Agentic AI": "quizzes/agentic ai_quiz.json",
    "Machine Learning": "quizzes/machine_learning_quiz.json",
    "Deep Learning": "quizzes/deep_learning_quiz.json",
    "Generative AI": "quizzes/generative_ai_quiz.json",
    "Prompt Engineering": "quizzes/prompt_engineering_quiz.json"
}

# Session State
if "completed_concepts" not in st.session_state:
    st.session_state.completed_concepts = {}

# Helper Function
def get_total_concepts(topic_file):
    try:
        with open(topic_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        count = 0
        if "subtopics" in data:
            for subtopic in data["subtopics"].values():
                count += len(
                    subtopic.get(
                        "concepts",
                        {}
                    )
                )
        else:
            count = len(
                data.get(
                    "concepts",
                    {}
                )
            )
        return count
    except Exception:
        return 0

# Sidebar
st.sidebar.title("📚 AI Learning Hub")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Learn", "Quiz"]
)

# HOME PAGE
if page == "Home":
    st.title("🤖 AI Learning Hub")
    st.markdown(""" 
    Welcome to the **AI Learning Hub**. Master Artificial Intelligence, One Step at a Time.

    This platform will help you in exploring AI concepts, discover cutting-edge technologies, test your knowledge through interactive quizzes, and track your learning journey in one place.:

    ✅ Learn AI Concepts

    ✅ Explore AI Technologies

    ✅ Understand Key Concepts

    ✅ Track Learning Progress

    ✅ Test Knowledge Through Quizzes

    ---

    Use the navigation menu on the left to get started.
    """)

# LEARN PAGE
elif page == "Learn":
    st.title("📖 Learn AI Topics")

    # Overall Learning Progress
    total_concepts_all_topics = 0
    completed_concepts_all_topics = 0

    for topic, file_path in topic_files.items():
        total_concepts_all_topics += get_total_concepts(
            file_path
        )
        completed_concepts_all_topics += len(
            st.session_state.completed_concepts.get(
                topic,
                []
            )
        )

    overall_progress = 0
    if total_concepts_all_topics > 0:
        overall_progress = int(
            (
                completed_concepts_all_topics
                / total_concepts_all_topics
            ) * 100
        )

    st.markdown("### 📊 Overall Learning Progress")
    st.progress(overall_progress)
    st.caption(
        #f"{completed_concepts_all_topics} of {total_concepts_all_topics} concepts completed ({overall_progress}%)"
        f"Overall Completion ({overall_progress}%)"
    )

    st.markdown("---")

    # Topic Dropdown
    display_topics = []
    for topic, file_path in topic_files.items():
        total_topic_concepts = get_total_concepts(
            file_path
        )

        completed_topic_concepts = len(
            st.session_state.completed_concepts.get(
                topic,
                []
            )
        )

        if (
            total_topic_concepts > 0
            and completed_topic_concepts
            >= total_topic_concepts
        ):

            display_topics.append(
                f"✅ {topic}"
            )
        else:
            display_topics.append(
                topic
            )

    selected_display = st.selectbox(
        "Choose a Topic",
        display_topics
    )

    selected_topic = selected_display.replace(
        "✅ ",
        ""
    )

    filepath = topic_files[selected_topic]

    if os.path.exists(filepath):
        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            topic_data = json.load(file)

        st.subheader(selected_topic)

        st.write(
            topic_data.get(
                "description",
                "No description available."
            )
        )

        # Concepts Handling

        concepts = {}

        if "subtopics" in topic_data:
            st.markdown("---")
            selected_subtopic = st.selectbox(
                "Choose a Subtopic",
                list(
                    topic_data["subtopics"].keys()
                )
            )

            concepts = (
                topic_data["subtopics"]
                .get(
                    selected_subtopic,
                    {}
                )
                .get(
                    "concepts",
                    {}
                )
            )

        else:
            concepts = topic_data.get(
                "concepts",
                {}
            )

        st.markdown("---")
        st.markdown(
            "## 🔑 Key Concepts"
        )

        if not concepts:
            st.warning(
                "No concepts found."
            )

        else:
            if (
                selected_topic
                not in st.session_state.completed_concepts
            ):
                st.session_state.completed_concepts[
                    selected_topic
                ] = []

            completed_list = (
                st.session_state.completed_concepts[
                    selected_topic
                ]
            )

            concept_options = []

            for concept in concepts.keys():

                if concept in completed_list:
                    concept_options.append(
                        f"✅ {concept}"
                    )
                else:
                    concept_options.append(
                        concept
                    )

            selected_display_concept = st.selectbox(
                "Select a Concept",
                concept_options
            )

            selected_concept = (
                selected_display_concept.replace(
                    "✅ ",
                    ""
                )
            )

            st.markdown("### Definition")
            st.info(
                concepts[selected_concept]
            )

            # Topic Progress
            total_topic_concepts = get_total_concepts(
                filepath
            )

            completed_topic_concepts = len(
                completed_list
            )

            topic_progress = int(
                (
                    completed_topic_concepts
                    / total_topic_concepts
                ) * 100
            )

            st.markdown(
                "### 📈 Topic Progress"
            )

            st.progress(
                topic_progress
            )

            st.caption(
                f"{completed_topic_concepts} of {total_topic_concepts} concepts completed ({topic_progress}%)"
            )

            st.markdown("---")

            # Concept Completion
            if (
                selected_concept
                in completed_list
            ):

                st.success(
                    f"✅ {selected_concept} completed"
                )

            else:

                if st.button(
                    f"Mark '{selected_concept}' Complete ✅",
                    use_container_width=True
                ):

                    completed_list.append(
                        selected_concept
                    )

                    st.rerun()

            # Topic Completed
            if (
                total_topic_concepts > 0
                and completed_topic_concepts
                >= total_topic_concepts
            ):

                st.success(
                    f"🎉 Congratulations! '{selected_topic}' completed."
                )

    else:
        st.error(
            f"Topic file not found: {filepath}"
        )

# QUIZ PAGE
elif page == "Quiz":

    st.title(
        "📝 AI Knowledge Check"
    )

    selected_topic = st.selectbox(
        "Select Topic to Test your knowledge",
        list(quiz_files.keys())
    )

    quiz_path = quiz_files[selected_topic]

    if os.path.exists(quiz_path):
        with open(
            quiz_path,
            "r",
            encoding="utf-8"
        ) as f:
            quiz_data = json.load(f)

        questions = quiz_data.get(
            "quiz",
            []
        )
        # Pick only 5 random questions if more than 5 exist
        if len(questions) > 5:
            questions = random.sample(
                questions,
                5
            )

        if not questions:
            st.warning(
                f"No quiz found for {selected_topic}"
            )

        else:
            score = 0
            with st.form(
                f"{selected_topic}_quiz_form"
            ):

                answers = []

                for idx, q in enumerate(
                    questions
                ):

                    answer = st.radio(
                        q["question"],
                        q["options"],
                        index=None,
                        key=f"{selected_topic}_{idx}"
                    )

                    answers.append(
                        answer
                    )

                submitted = st.form_submit_button(
                    "Submit Quiz"
                )

            if submitted:
                for user_answer, question in zip(
                    answers,
                    questions
                ):

                    if (
                        user_answer
                        == question["answer"]
                    ):
                        score += 1

                total = len(
                    questions
                )

                percentage = (
                    score / total
                ) * 100

                #st.success(
                #    f"Score: {score}/{total}"
                attempted = len(
                    [a for a in answers if a is not None]
                )

                correct = score

                wrong = 0

                for user_answer, question in zip(
                        answers,
                        questions
                ):

                    if user_answer is not None:

                        if user_answer != question["answer"]:
                            wrong += 1

                unanswered = total - attempted

                st.success(
                    f"Score: {correct}/{total}"
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Questions Attempted",
                        f"{attempted}/{total}"
                    )

                with col2:
                    st.metric(
                        "✅ Correct",
                        correct
                    )

                with col3:
                    st.metric(
                        "❌ Wrong",
                        wrong
                    )

                with col4:
                    st.metric(
                        "⚪ Unanswered",
                        unanswered
                    )

                st.progress(
                    int(
                        percentage
                    )
                )

                if percentage >= 80:
                    st.balloons()

                    st.success(
                        "Excellent! 🎉"
                    )

                elif percentage >= 50:
                    st.info(
                        "Good Job! 👍"
                    )

                else:
                    st.warning(
                        "Keep Practicing 📚"
                    )

                st.markdown(
                    "---"
                )

                st.subheader(
                    "✅ Correct Answers"
                )

                for q in questions:
                    st.write(
                        f"**{q['question']}**"
                    )
                    st.write(
                        f"Answer: {q['answer']}"
                    )
                    st.write(
                        "---"
                    )

    else:
        st.error(
            f"Quiz file not found: {quiz_path}"
        )