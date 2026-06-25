import streamlit as st
import requests
import json
import os
import pandas as pd
import plotly.express as px
from app.services.intake_pipeline import (
    IntakePipeline
)

from app.services.uploaded_dataset_inspector import (
    UploadedDatasetInspector
)

from app.services.dashboard_data_provider import (
    DashboardDataProvider
)

from app.services.optimization_pipeline import (
    OptimizationPipeline
)

from app.services.optimization_report_manager import (
    OptimizationReportManager
)

st.set_page_config(
    page_title="AgentDLOps",
    layout="wide"
)

st.title("AgentDLOps Dashboard")
st.subheader(
    "Autonomous Deep Learning Optimization Platform"
)

# ----------------------------------
# SIDEBAR
# ----------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Autonomous Project",
        "Project Intake",
        "Architecture Benchmark",
        "Hyperparameter Benchmark",
        "Champion Model",
        "Deployment",
        "Decision Report",
        "Historical Analytics",
        "Agent Monitor",
        "Training Monitor",
        "API Health"
    ]
)

# ----------------------------------
# AUTONOMOUS PROJECT
# ----------------------------------

if page == "Autonomous Project":

    from app.services.autonomous_pipeline import (
        AutonomousPipeline
    )

    st.header(
        "AgentDLOps Autonomous Execution"
    )

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["zip", "csv"]
    )

    problem_type = st.selectbox(
        "Problem Type",
        [
            "image_classification",
            "regression",
            "tabular_classification",
            "object_detection",
            "nlp_classification"
        ]
    )

    problem_statement = st.text_area(
        "Problem Statement"
    )

    expected_outcome = st.text_input(
        "Expected Outcome"
    )

    dataset_type = st.selectbox(
        "Dataset Type",
        [
            "image",
            "tabular",
            "text",
            "audio",
            "video"
        ]
    )

    deployment_target = st.selectbox(
        "Deployment Target",
        [
            "cloud",
            "mobile",
            "edge",
            "web_api"
        ]
    )

    optimization_priority = st.selectbox(
        "Optimization Priority",
        [
            "accuracy",
            "latency",
            "cost",
            "memory"
        ]
    )

    if st.button(
        "🚀 Run Autonomous Project"
    ):

        if not uploaded_file:

            st.error(
                "Please upload a dataset."
            )

        else:

            os.makedirs(
                "uploads",
                exist_ok=True
            )

            dataset_path = (
                f"uploads/{uploaded_file.name}"
            )

            with open(
                dataset_path,
                "wb"
            ) as file:

                file.write(
                    uploaded_file.getbuffer()
                )

            project_context = {

                "problem_type":
                    problem_type,

                "problem_statement":
                    problem_statement,

                "expected_outcome":
                    expected_outcome,

                "dataset_type":
                    dataset_type,

                "deployment_target":
                    deployment_target,

                "optimization_priority":
                    optimization_priority
            }

            pipeline = (
                AutonomousPipeline()
            )

            with st.spinner(
                "Running AgentDLOps..."
            ):

                result = (
                    pipeline.run(
                        dataset_path,
                        project_context
                    )
                )

            st.success(
                "Autonomous Execution Complete"
            )

            best_model = (
                result[
                    "optimization_result"
                ][
                    "best_architecture"
                ]
            )

            decision = (
                result[
                    "control_result"
                ][
                    "workflow_result"
                ][
                    "decision"
                ]
            )

            col1,col2,col3 = st.columns(3)

            with col1:

                st.metric(
                    "Champion Model",
                    best_model["model"]
                )

            with col2:

                st.metric(
                    "Accuracy",
                    f"{best_model['accuracy']:.2f}%"
                )

            with col3:

                st.metric(
                    "LLM Decision",
                    decision["action"]
                )

            st.subheader(
                "Dataset Analysis"
            )

            st.subheader(
                "Execution Timeline"
            )

            st.success(
                "✓ Dataset Analysis"
            )

            st.success(
                "✓ Project Intake"
            )

            st.success(
                "✓ Architecture Search"
            )

            st.success(
                "✓ Hyperparameter Optimization"
            )

            st.success(
                "✓ Control Tower Decision"
            )

            st.success(
                "✓ Workflow Execution"
            )

            st.success(
                "✓ Memory Update"
            )

            st.success(
                "✓ Research Paper Generation"
            )

            st.json(
                result[
                    "dataset_report"
                ]
            )

            st.subheader(
                "Optimization Result"
            )

            architecture_results = (
                result[
                    "optimization_result"
                ].get(
                    "architecture_results",
                    []
                )
            )

            if architecture_results:

                df = pd.DataFrame(
                    architecture_results
                )

                st.dataframe(
                    df,
                    width="stretch"
                )

            st.json(
                result[
                    "optimization_result"
                ]
            )

            st.subheader(
                "Control Tower"
            )

            st.json(
                result[
                    "control_result"
                ]
            )

            st.subheader(
                "Learning"
            )

            st.json(
                result[
                    "learning_result"
                ]
            )

            st.subheader(
                "Research Report"
            )

            st.markdown(
                result[
                    "research_paper"
                ]
            )

# ----------------------------------
# PROJECT INTAKE
# ----------------------------------

if page == "Project Intake":

    st.header("Project Intake Form")

    problem_type = st.selectbox(
        "Problem Type",
        [
            "Image Classification",
            "Regression",
            "Tabular Classification",
            "Object Detection",
            "NLP Classification"
        ]
    )

    problem_statement = st.text_area(
        "Problem Statement"
    )

    expected_outcome = st.text_input(
        "Expected Outcome"
    )

    dataset_type = st.selectbox(
        "Dataset Type",
        [
            "Image",
            "Tabular",
            "Text",
            "Audio",
            "Video"
        ]
    )

    deployment_target = st.selectbox(
        "Deployment Target",
        [
            "Cloud",
            "Mobile",
            "Edge",
            "Web API"
        ]
    )

    optimization_priority = st.selectbox(
        "Optimization Priority",
        [
            "Accuracy",
            "Latency",
            "Cost",
            "Memory"
        ]
    )
    uploaded_file = st.file_uploader(

        "Upload Dataset",

        type=[
            "csv",
            "zip"
        ]
    )

    if st.button(
        "Submit Project"
    ):

        save_path = None

        if uploaded_file:

            os.makedirs(
                "uploads",
                exist_ok=True
            )

            save_path = (

                "uploads/"
                f"{uploaded_file.name}"
            )

            with open(
                save_path,
                "wb"
            ) as file:

                file.write(
                    uploaded_file.getbuffer()
                )

            inspector = (
                UploadedDatasetInspector()
            )

            dataset_report = (
                inspector.inspect(
                    save_path
                )
            )

            st.subheader(
                "Dataset Analysis"
            )

            st.json(
                dataset_report
            )

        pipeline = (
            IntakePipeline()
        )

        result = (
            pipeline.execute(

                problem_type
                .lower()
                .replace(
                    " ",
                    "_"
                ),

                problem_statement,

                expected_outcome,

                dataset_type
                .lower(),

                deployment_target
                .lower(),

                optimization_priority
                .lower()
            )
        )

        st.success(
            "Pipeline Executed"
        )

        st.subheader(
            "Candidate Models"
        )

        st.json(
            result[
                "candidate_result"
            ]
        )

        st.subheader(
            "Deployment Strategy"
        )

        st.json(
            result[
                "deployment_result"
            ]
        )

        st.subheader(
            "Decision Report"
        )

        st.json(
            result[
                "decision"
            ]
        )

    if st.button(
        "Run Optimization"
    ):

        with st.spinner(
            "Running architecture benchmark..."
        ):

            optimizer = (
                OptimizationPipeline()
            )

            intake_report = {
                "problem_type":
                    problem_type
                    .lower()
                    .replace(" ", "_"),

                "dataset_type":
                    dataset_type.lower(),

                "deployment_target":
                    deployment_target.lower(),

                "optimization_priority":
                    optimization_priority.lower()
            }

            optimization_result = (
                optimizer.execute(
                    intake_report
                )
            )

        st.success(
            "Optimization Completed"
        )

        st.subheader(
            "Best Architecture"
        )

        st.json(
            optimization_result[
                "best_architecture"
            ]
        )

        st.subheader(
            "Best Hyperparameter"
        )

        st.json(
            optimization_result[
                "best_hyperparameter"
            ]
        )

        manager = (
            OptimizationReportManager()
        )

        manager.save(
            optimization_result
        )

# ----------------------------------
# ARCHITECTURE BENCHMARK
# ----------------------------------

elif page == "Architecture Benchmark":

    st.header(
        "Architecture Benchmark Results"
    )

    report_path = (
        "reports/optimization_report.json"
    )

    if os.path.exists(
        report_path
    ):

        with open(
            report_path,
            "r"
        ) as file:

            report = json.load(
                file
            )

        st.json(
            report[
                "best_architecture"
            ]
        )

    else:

        st.warning(
            "Run optimization first."
        )
# ----------------------------------
# HYPERPARAMETER BENCHMARK
# ----------------------------------

elif page == "Hyperparameter Benchmark":

    st.header(
        "Hyperparameter Benchmark Results"
    )

    hp_results = [

        {
            "Learning Rate":
                0.001,

            "Accuracy":
                33.83
        },

        {
            "Learning Rate":
                0.0005,

            "Accuracy":
                30.42
        },

        {
            "Learning Rate":
                0.0001,

            "Accuracy":
                18.53
        }
    ]

    st.dataframe(
        hp_results
    )

# ----------------------------------
# CHAMPION MODEL
# ----------------------------------

elif page == "Champion Model":

    st.header(
        "Champion Model"
    )

    st.success(
        "Current Champion"
    )

    st.metric(
        label="Model",
        value="ResNet50"
    )

    st.metric(
        label="Accuracy",
        value="33.83%"
    )

# ----------------------------------
# DEPLOYMENT
# ----------------------------------

elif page == "Deployment":

    st.header(
        "Deployment Recommendation"
    )

    deployment = {

        "Platform":
            "TorchServe",

        "Format":
            ".pth",

        "Reason":
            "High accuracy server inference"
    }

    st.json(
        deployment
    )

# ----------------------------------
# DECISION REPORT
# ----------------------------------

elif page == "Decision Report":

    st.header(
        "Final Decision Report"
    )

    report_path = (
        "reports/final_decision_report.json"
    )

    if os.path.exists(
        report_path
    ):

        with open(
            report_path,
            "r"
        ) as file:

            report = json.load(
                file
            )

        st.json(
            report
        )

    else:

        st.warning(
            "No decision report found."
        )

elif page == "Historical Analytics":

    from app.services.project_analytics import (
        ProjectAnalytics
    )

    analytics = (
        ProjectAnalytics()
    )

    stats = (
        analytics.get_statistics()
    )

    st.header(
        "Historical Analytics"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Runs",
            stats["total_runs"]
        )

    with col2:

        st.metric(
            "Best Accuracy",
            stats["best_accuracy"]
        )

    st.subheader(
        "Architecture Usage"
    )

    architecture_usage = (
        stats[
            "architecture_usage"
        ]
    )

    if architecture_usage:

        df = pd.DataFrame(

            list(
                architecture_usage.items()
            ),

            columns=[
                "Architecture",
                "Count"
            ]
        )

        fig = px.bar(

            df,

            x="Architecture",

            y="Count",

            title="Architecture Usage"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        st.dataframe(
            df,
            width="stretch"
        )

    else:

        st.info(
            "No historical runs found."
        )

elif page == "Agent Monitor":

    import pandas as pd

    from app.services.agent_status_tracker import (
        AgentStatusTracker
    )

    tracker = (
        AgentStatusTracker()
    )

    st.header(
        "Live Agent Monitoring Dashboard"
    )

    status = (
        tracker.get_status()
    )

    if not status:

        st.info(
            "No agent activity yet."
        )

    else:

        status_df = pd.DataFrame(

            list(
                status.items()
            ),

            columns=[
                "Agent",
                "Status"
            ]
        )

        st.dataframe(
            status_df,
            width="stretch"
        )

        for agent, state in status.items():

            if state == "Completed":

                st.success(
                    f"{agent} : {state}"
                )

            elif state == "Running":

                st.warning(
                    f"{agent} : {state}"
                )

            else:

                st.info(
                    f"{agent} : {state}"
                )

elif page == "Training Monitor":

    from app.services.training_state import (
        TrainingState
    )

    st.header(
        "Live Training Monitor"
    )

    from streamlit_autorefresh import (
        st_autorefresh
    )

    st_autorefresh(
        interval=2000,
        key="training_refresh"
    )

    state = (
        TrainingState()
        .get_state()
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Model",
            state["model"]
        )

        st.metric(
            "Epoch",
            state["epoch"]
        )

    with col2:

        st.metric(
            "Loss",
            round(
                state["loss"],
                4
            ) if state["loss"] else 0
        )

        st.metric(
            "Status",
            state["status"]
        )

    st.json(
        state
    )

# ----------------------------------
# API HEALTH
# ----------------------------------

elif page == "API Health":

    st.header(
        "FastAPI Health Check"
    )

    if st.button(
        "Check API"
    ):

        try:

            response = requests.get(
                "http://127.0.0.1:8000/health"
            )

            st.success(
                "API Connected"
            )

            st.json(
                response.json()
            )

        except Exception as e:

            st.error(
                f"Connection Failed: {e}"
            )