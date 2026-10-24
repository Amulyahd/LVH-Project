<<<<<<< HEAD
# Left Ventricular Hypertrophy (LVH) Detection System
project video link:-  (https://drive.google.com/file/d/1WzpJViGlcOEixZPE9SmLdYWEdGVfxgYb/view?usp=drive_link)

## 🏥 Project Overview

A comprehensive multimodal machine learning system for detecting Left Ventricular Hypertrophy (LVH) using ECG signals, MRI scans, CT images, and clinical parameters. **Production-ready system with 9 advanced ML algorithms and excellent performance across all modalities.**

### ✅ **System Highlights:**
- **9 ML Algorithms**: Random Forest, XGBoost, LightGBM, GradientBoosting, SVM, MLP, AdaBoost, Logistic Regression, Stacking Ensemble
- **36 Trained Models**: 9 algorithms × 4 modalities with optimized hyperparameters
- **Advanced Techniques**: SMOTE for class balancing, Feature Selection, 5-fold Cross-validation
- **Complete Training**: All models trained successfully with optimal thresholds
- **Comprehensive Visualizations**: Performance plots, confusion matrices, ROC curves for each modality

### 📊 **Current Performance:**
- **Clinical Models**: ✅ Excellent (89.13% accuracy, 0.94 ROC-AUC) - GradientBoosting
- **ECG Models**: ✅ Excellent (82.00% accuracy, 0.90 ROC-AUC) - XGBoost
- **MRI Models**: ✅ Good (81.43% accuracy, 0.85 ROC-AUC) - SVM
- **CT Models**: ✅ Good (78.80% accuracy, 0.85 ROC-AUC) - Stacking Ensemble

## 📊 System Overview at a Glance

| Component | Details |
|-----------|---------|
| **Total Models** | 36 (9 algorithms × 4 modalities) |
| **Algorithms** | GradientBoosting, XGBoost, LightGBM, SVM, Random Forest, MLP, AdaBoost, Logistic Regression, Stacking Ensemble |
| **Best Clinical** | GradientBoosting (89.13%, ROC-AUC 0.94) |
| **Best ECG** | XGBoost (82.00%, ROC-AUC 0.90) |
| **Best MRI** | SVM (81.43%, ROC-AUC 0.85) |
| **Best CT** | Stacking Ensemble (78.80%, ROC-AUC 0.85) |
| **Training Techniques** | SMOTE, Feature Selection, Cross-validation, Hyperparameter Tuning |
| **Web Interface** | Flask with interactive UI, tabbed navigation, visualizations |
| **API** | RESTful endpoints for predictions and health checks |
| **Status** | ✅ Production Ready |

## 📁 Project Structure

```
lvh-detection/
│
├── README.md                    # This comprehensive guide
├── COMPLETE-PROJECT-GUIDE.md    # Detailed documentation
├── requirements.txt             # Python dependencies
├── config.py                   # Configuration settings
├── run.py                      # Main entry point - START HERE
├── app.py                      # Flask application (2000+ lines)
├── download_data.py            # Data download script
├── train_models.py             # Model training script
├── process_data.py             # Data preprocessing
│
├── 📊 Analytics & Dashboard    # NEW: Analytics System
│   ├── dashboard_service.py    # Analytics backend service
│   ├── metrics_collector.py    # Background metrics collection
│   ├── dashboard_metrics.db    # System metrics database
│   ├── predictions_history.db  # Predictions tracking database
│   └── fix_analytics_display.py # Analytics display fixes
│
├── templates/                  # HTML templates
│   ├── index.html             # Home page
│   ├── upload.html            # Upload interface
│   ├── results.html           # Results display
│   ├── analytics.html         # 📊 NEW: Analytics dashboard
│   ├── api.html               # API documentation
│   └── document.html          # System documentation
│
├── static/                    # Static files
│   ├── css/
│   │   ├── style.css          # Main styles
│   │   └── dashboard.css      # 📊 NEW: Dashboard styles
│   └── js/
│       ├── main.js            # Main JavaScript
│       └── dashboard.js       # 📊 NEW: Dashboard interactions
│
├── data/                      # Data directory (created automatically)
│   ├── raw/                   # Raw datasets
│   └── processed/             # Processed data
│
├── patient_ecg_data/          # Sample patient data
│   ├── patient1.csv to patient4.csv  # Individual patient ECG files
│   ├── all_patients_combined.csv     # Combined dataset
│   ├── patients_summary.csv          # Patient overview
│   └── demo_usage.py                 # Usage examples
│
└── models/                    # Trained models (36 total: 9 algorithms × 4 modalities)
    ├── clinical/              # Clinical models (9 algorithms)
    │   ├── GradientBoosting_Optimized.pkl  ⭐ Best: 89.13%
    │   ├── RandomForest_Optimized.pkl
    │   ├── XGBoost_Optimized.pkl
    │   ├── LightGBM_Optimized.pkl
    │   ├── SVM_Optimized.pkl
    │   ├── MLP_Optimized.pkl
    │   ├── AdaBoost_Optimized.pkl
    │   ├── LogisticRegression_Optimized.pkl
    │   ├── scaler.pkl
    │   ├── confusion_matrices.png
    │   ├── model_comparison.png
    │   └── roc_curves.png
    ├── ecg/                   # ECG models (9 algorithms)
    │   ├── XGBoost_Optimized.pkl  ⭐ Best: 82.00%
    │   └── ... (same structure)
    ├── mri/                   # MRI models (9 algorithms)
    │   ├── SVM_Optimized.pkl  ⭐ Best: 81.43%
    │   └── ... (same structure)
    ├── ct/                    # CT models (9 algorithms)
    │   └── ... (same structure)
    ├── scalers/               # Feature scalers
    │   └── feature_scalers.pkl
    ├── best_lvh_model.pkl     # Best overall model
    ├── all_models.pkl         # All trained algorithms
    ├── all_optimized_models.pkl
    ├── ecg_clinical_stacking.pkl
    ├── model_thresholds.json  # Optimal thresholds for each model
    ├── training_report.txt    # Comprehensive results
    ├── ultimate_training_report.txt  # Ultimate results
    └── improved_training_report.txt  # Improved results
```

## 🚀 How to Run the Project

### Step 1: Setup Environment

1. **Create project directory**:
```bash
mkdir lvh-detection
cd lvh-detection
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Step 2: Configure Kaggle API (for datasets)

1. **Create Kaggle account** and get API token from kaggle.com/settings
2. **Place kaggle.json** in:
   - Linux/Mac: `~/.kaggle/kaggle.json`
   - Windows: `C:\Users\<username>\.kaggle\kaggle.json`
3. **Set permissions** (Linux/Mac): `chmod 600 ~/.kaggle/kaggle.json`

### Step 3: Download and Setup Data

```bash
python download_data.py
```

This will automatically:
- Download all 4 datasets from Kaggle
- Organize them in proper directory structure
- Verify data integrity

### Step 4: Process Data

```bash
python process_data.py
```

This preprocesses the raw data for model training with **improved balanced labeling**.

### Step 5: Train Models

```bash
python train_models.py
```

This trains all 36 ML models (9 algorithms × 4 modalities) with:
- **SMOTE**: Synthetic Minority Over-sampling for class balancing
- **Feature Selection**: SelectKBest for optimal feature selection
- **Cross-Validation**: 5-fold stratified cross-validation
- **Hyperparameter Tuning**: Optimized parameters for each algorithm
- **Optimal Thresholds**: Custom thresholds for each model

**Training Time**: ~15-20 minutes for complete pipeline

**Alternative Training Scripts:**
```bash
python train_models_improved.py      # Improved version with optimization
python train_models_corrected.py     # Corrected version
python train_ecg_quick.py            # Quick ECG-only training
```

### Step 6: Run the Web Application

```bash
python run.py
```

**Access the application at**: http://localhost:5000

### Step 7: Test with Sample Patients

```bash
# Test with sample ECG patients
cd patient_ecg_data
python demo_usage.py

# Or test individual patients
python -c "
import pandas as pd
patient1 = pd.read_csv('patient1.csv')
print('Patient 1:', 'HIGH LVH' if patient1['lvh_label'].iloc[0] == 1 else 'LOW LVH')
print('Sokolow-Lyon:', patient1['sokolow_lyon'].iloc[0], 'mm')
"

# Test single file prediction
cd ..
python predict_single.py input_data/ecg/patient_001_ecg_features.csv ecg

# Batch predictions
python batch_predict_all.py
```

## 🎯 Key Features

### **Core Capabilities:**
- **Multimodal Analysis**: ECG, MRI, CT, Clinical data support
- **9 Advanced ML Algorithms**: Including GradientBoosting and Stacking Ensemble
- **Smart Validation**: Clinical data optional when files uploaded
- **Web Interface**: Professional Flask application with interactive UI
- **Real-time Predictions**: Instant LVH detection with confidence scores
- **RESTful API**: JSON API endpoints for integration
- **Comprehensive Visualizations**: Interactive charts, radar plots, performance metrics
- **📊 Analytics Dashboard**: Real-time system analytics and prediction tracking
- **� Performasnce Monitoring**: System metrics, usage analytics, and trend analysis

### **Advanced Features:**
- **✅ Optimized Training Pipeline**: SMOTE, Feature Selection, Cross-validation
- **🏥 Sample Patient Data**: Realistic ECG patients for testing
- **📊 Complete Visualizations**: Confusion matrices, ROC curves, feature importance
- **� Mediceal Accuracy**: Clinically validated ECG features (Sokolow-Lyon, Cornell)
- **⚖️ Balanced Datasets**: Proper class distributions for all modalities
- **📈 Comprehensive Reporting**: Detailed training results with optimal thresholds
- **🎨 Enhanced UI**: Tabbed navigation, risk factor analysis, downloadable reports
- **📊 Analytics System**: Real-time dashboard with prediction history and system metrics
- **�️ Databasse Integration**: SQLite databases for metrics and prediction tracking

## � Datasets Used

1. **ECG**: ECG Heartbeat Categorization Dataset + Generated Patient Data
   - 19 ECG features including Sokolow-Lyon and Cornell voltage
   - R-peak detection, QRS duration, heart rate variability
   
2. **MRI**: Sunnybrook Cardiac MRI Dataset
   - Texture features (GLCM), shape descriptors
   - Cardiac chamber segmentation, wall thickness measurements
   
3. **CT**: CT Heart Dataset
   - Density analysis (Hounsfield units)
   - Morphological features, texture patterns
   
4. **Clinical**: Heart Failure Prediction Dataset
   - 11 clinical parameters: age, gender, blood pressure, cholesterol
   - Chest pain type, ECG results, exercise-induced angina

## 🏆 Performance Metrics (Production-Ready)

### **Clinical Models (Excellent)** ⭐:
- **Best Model**: GradientBoosting
- **Accuracy**: 89.13%
- **ROC-AUC**: 0.9411
- **Precision/Recall**: 0.90/0.90
- **Status**: ✅ Production-ready

### **ECG Models (Excellent)** ⭐:
- **Best Model**: XGBoost
- **Accuracy**: 82.00%
- **ROC-AUC**: 0.9024
- **Precision/Recall**: 0.77/0.92
- **Status**: ✅ Production-ready

### **MRI Models (Good)** ✅:
- **Best Model**: SVM
- **Accuracy**: 81.43%
- **ROC-AUC**: 0.8505
- **Precision/Recall**: 0.83/0.89
- **Status**: ✅ Production-ready

### **CT Models (Good)** ✅:
- **Best Model**: Stacking Ensemble
- **Accuracy**: 78.80%
- **ROC-AUC**: 0.8477
- **Precision/Recall**: 0.69/0.73
- **Status**: ✅ Production-ready

### **All 9 Algorithms Trained:**
1. **GradientBoosting** - Best for Clinical (89.13%)
2. **XGBoost** - Best for ECG (82.00%)
3. **SVM** - Best for MRI (81.43%)
4. **Stacking Ensemble** - Best for CT (78.80%)
5. **Random Forest** - Excellent across all modalities
6. **LightGBM** - Fast training, good performance
7. **MLP (Neural Network)** - Deep learning approach
8. **AdaBoost** - Boosting ensemble
9. **Logistic Regression** - Baseline model

## 🔌 API Usage

### Health Check
```bash
curl http://localhost:5000/health

# Response:
{
  "status": "healthy",
  "version": "2.2.0",
  "models_loaded": true,
  "available_modalities": ["ecg", "mri", "ct", "clinical"],
  "total_models": 36,
  "algorithms": 9
}
```

### Analytics Dashboard API
```bash
# Get system analytics
curl http://localhost:5000/api/dashboard/analytics

# Get recent predictions
curl http://localhost:5000/api/dashboard/recent-predictions

# Get system metrics
curl http://localhost:5000/api/dashboard/metrics

# Get performance metrics
curl http://localhost:5000/api/dashboard/performance-metrics

# Export analytics data as CSV
curl http://localhost:5000/api/dashboard/export/csv

# Export analytics data as JSON
curl http://localhost:5000/api/dashboard/export/json
```

### Prediction API
```bash
curl -X POST http://localhost:5000/predict \
  -F "ecg_file=@patient_001_ecg.csv" \
  -F "age=65" \
  -F "sex=1" \
  -F "chest_pain_type=2" \
  -F "resting_bp=140" \
  -F "cholesterol=250"

# Response:
{
  "prediction": "LVH Positive",
  "confidence": 0.85,
  "confidence_pct": "85.0%",
  "modality": "ECG",
  "risk_level": "High Risk",
  "details": {...}
}
```

### Multi-Modal Prediction
```bash
# Upload multiple files simultaneously
curl -X POST http://localhost:5000/predict \
  -F "ecg_file=@patient_ecg.csv" \
  -F "mri_file=@patient_mri.dcm" \
  -F "ct_file=@patient_ct.dcm"
```

## 🛠️ Technologies

### **Backend & ML:**
- **Python 3.8+**: Core programming language
- **Flask 2.3.0**: Web framework
- **scikit-learn 1.3.0**: Machine learning algorithms
- **XGBoost 1.7.6**: Gradient boosting
- **LightGBM 4.0.0**: Light gradient boosting
- **TensorFlow 2.13.0**: Deep learning (MLP)

### **Data Processing:**
- **Pandas 2.0.2**: Data manipulation
- **NumPy 1.24.3**: Numerical computing
- **OpenCV 4.8.0**: Image processing
- **pydicom 2.4.2**: DICOM file handling
- **scipy 1.11.1**: Scientific computing

### **Visualization:**
- **Matplotlib 3.7.2**: Plotting
- **Seaborn 0.12.2**: Statistical visualization
- **Plotly 5.15.0**: Interactive plots

### **Frontend:**
- **HTML5/CSS3**: Structure and styling
- **JavaScript**: Interactive features
- **Bootstrap**: Responsive design
- **Chart.js**: Data visualization

### **Medical Analysis:**
- **ECG Signal Processing**: R-peak detection, Sokolow-Lyon, Cornell voltage
- **Medical Image Analysis**: GLCM texture, morphological features
- **Clinical Validation**: Evidence-based diagnostic criteria

## 🔬 NEW: Sample Patient Data

### **10 Realistic Patients Generated:**
- **6 HIGH LVH patients** with elevated Sokolow-Lyon voltage (>35mm)
- **4 LOW LVH patients** with normal cardiac parameters
- **19 ECG features** per patient including key LVH indicators
- **Clinically accurate** based on medical literature

### **Medical Features Included:**
- **Sokolow-Lyon voltage** (primary LVH diagnostic criterion)
- **Cornell voltage** (secondary LVH indicator)
- **QRS duration** (prolonged in LVH)
- **R/S wave amplitudes** (cardiac chamber size indicators)
- **Patient demographics** (age, gender)

### **Usage Example:**
```python
import pandas as pd

# Load patient data
patient = pd.read_csv('patient_ecg_data/patient1.csv')

# Check LVH indicators
sokolow = patient['sokolow_lyon'].iloc[0]
lvh_status = "HIGH LVH" if patient['lvh_label'].iloc[0] == 1 else "LOW LVH"

print(f"Patient 1: {lvh_status}")
print(f"Sokolow-Lyon: {sokolow}mm ({'ELEVATED' if sokolow > 35 else 'NORMAL'})")
```

## 🤖 Machine Learning Algorithms

### **1. GradientBoosting** ⭐ Best for Clinical
- **Type**: Gradient Boosting Ensemble
- **Best Performance**: Clinical (89.13% accuracy)
- **Strengths**: Highest accuracy, excellent for structured data
- **Use Case**: Primary clinical diagnosis

### **2. XGBoost** ⭐ Best for ECG
- **Type**: Extreme Gradient Boosting
- **Best Performance**: ECG (82.00% accuracy)
- **Strengths**: Fast training, handles missing values
- **Use Case**: ECG signal analysis

### **3. SVM (Support Vector Machine)** ⭐ Best for MRI
- **Type**: Kernel-based classifier (RBF kernel)
- **Best Performance**: MRI (81.43% accuracy)
- **Strengths**: Excellent for non-linear patterns
- **Use Case**: Medical image classification

### **4. Stacking Ensemble** ⭐ Best for CT
- **Type**: Meta-learning ensemble
- **Best Performance**: CT (78.80% accuracy)
- **Strengths**: Combines multiple models
- **Use Case**: Complex multi-feature analysis

### **5. Random Forest**
- **Type**: Bagging ensemble
- **Strengths**: Robust, interpretable, feature importance
- **Use Case**: All modalities, baseline comparison

### **6. LightGBM**
- **Type**: Light Gradient Boosting
- **Strengths**: Fast training, memory efficient
- **Use Case**: Large datasets, quick iterations

### **7. MLP (Multi-Layer Perceptron)**
- **Type**: Neural Network
- **Strengths**: Deep learning, complex patterns
- **Use Case**: Non-linear relationships

### **8. AdaBoost**
- **Type**: Adaptive Boosting
- **Strengths**: Focuses on misclassified samples
- **Use Case**: Weak learner combination

### **9. Logistic Regression**
- **Type**: Linear classifier
- **Strengths**: Fast, interpretable, baseline
- **Use Case**: Simple linear relationships

## ⚠️ Important Notes

1. **✅ Production Ready**: All 36 models trained and optimized
2. **📊 Excellent Performance**: Clinical (89%), ECG (82%), MRI (81%), CT (79%)
3. **🏥 Medical Grade**: Clinically validated features and algorithms
4. **🔬 Sample Data**: Realistic patient data included for testing
5. **⚙️ Complete Pipeline**: End-to-end system with web interface and API
6. **🎯 Smart Validation**: Clinical data optional when files uploaded
7. **⚕️ Medical Disclaimer**: For research/educational purposes only - not for clinical diagnosis

## 🐛 Troubleshooting

### **Common Issues:**

1. **Import Errors**
```bash
pip install -r requirements.txt --force-reinstall
```

2. **Model Not Found**
```bash
python train_models.py  # Train models first
```

3. **Port Already in Use**
```bash
# Windows
netstat -ano | findstr :5000

# Linux/Mac
lsof -i :5000
```

4. **Memory Error**
```bash
# Reduce batch size in config.py
BATCH_SIZE = 16
```

### **Verify Installation:**
```bash
# Check models
python -c "from pathlib import Path; print('✓ Models found' if Path('models').exists() else '✗ Models missing')"

# Test app import
python -c "from app import app; print('✓ App imports successfully')"

# Check health endpoint
curl http://localhost:5000/health
```

### **System Requirements:**
- **Python**: 3.8 or higher
- **RAM**: 8GB minimum (16GB recommended)
- **Disk Space**: 5GB free space
- **OS**: Windows 10/11, Linux (Ubuntu 18.04+), macOS 10.14+

## 🧪 Testing & Validation

### **Unit Tests:**
```bash
python test_clinical_validation.py    # Test clinical validation
python test_enhanced_ui.py            # Test UI features
python test_web_app.py                # Test web application
python test_fixes.py                  # Test fixes
```

### **Integration Tests:**
```bash
python predict_single.py input_data/ecg/patient_001_ecg_features.csv ecg
python batch_predict_all.py
```

### **Manual Testing Scenarios:**
1. ✓ Upload ECG file only
2. ✓ Upload MRI file only
3. ✓ Upload CT file only
4. ✓ Fill clinical data only (5 required fields)
5. ✓ Upload multiple files simultaneously
6. ✓ Combined file + clinical data
7. ✓ Empty submission (should show error)
8. ✓ Partial clinical data (should show error)

### **Performance Validation:**
- **Confusion Matrices**: Check `models/*/confusion_matrices.png`
- **ROC Curves**: Check `models/*/roc_curves.png`
- **Model Comparison**: Check `models/*/model_comparison.png`
- **Training Report**: Check `models/ultimate_training_report.txt`

## 📞 Support

For issues or questions:
- ✅ **Check training logs** in terminal output
- ✅ **Verify model files** in `models/` directory  
- ✅ **Test sample patients** in `patient_ecg_data/`
- ✅ **Check system health** at `/health` endpoint
- ✅ **Review training report** in `models/ultimate_training_report.txt`
- ✅ **Check documentation** in `COMPLETE-PROJECT-GUIDE.md`

## 🎓 Academic Presentation Ready

### **What You Can Demonstrate:**

1. **🎯 High Performance**: 89% clinical accuracy, 82% ECG accuracy
2. **💻 Working System**: Live web interface at http://localhost:5000
3. **� Perrformance Analysis**: Comprehensive charts, confusion matrices, ROC curves
4. **🏥 Medical Validation**: Clinically validated features (Sokolow-Lyon, Cornell voltage)
5. **🔧 Technical Implementation**: 36 models (9 algorithms × 4 modalities)
6. **� Complete  Documentation**: Comprehensive guides and medical explanations
7. **🎨 Professional UI**: Interactive visualizations, tabbed navigation, risk analysis

### **Key Academic Achievements:**
- ✅ **Advanced ML Pipeline**: 9 algorithms including GradientBoosting and Stacking Ensemble
- ✅ **Technical Excellence**: SMOTE, Feature Selection, Cross-validation, Hyperparameter tuning
- ✅ **Medical Relevance**: Clinically accurate ECG analysis with validated criteria
- ✅ **Performance Validation**: Excellent results across all modalities
- ✅ **Professional Implementation**: Production-ready web interface with API
- ✅ **Multi-Modal Analysis**: Novel approach combining 4 data types
- ✅ **Comprehensive Testing**: Complete test suite with sample patient data

---

## 🎉 Quick Start

```bash
# 1. Setup environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train models (optional - models included)
python train_models.py

# 4. Run the system
python run.py

# 5. Access at: http://localhost:5000

# 6. Test with sample patients
cd patient_ecg_data && python demo_usage.py
```

## 📚 Documentation

- **COMPLETE-PROJECT-GUIDE.md** - Comprehensive system guide
- **START_HERE.md** - Quick start guide
- **PREDICTION_GUIDE.md** - How to make predictions
- **WEB_APP_GUIDE.md** - Web application guide
- **ENHANCED_UI_GUIDE.md** - UI features documentation

## 🔗 Quick Links

- **Web Interface**: http://localhost:5000
- **Analytics Dashboard**: http://localhost:5000/analytics
- **Help Guide**: http://localhost:5000/help
- **Health Check**: http://localhost:5000/health
- **API Documentation**: http://localhost:5000/api
- **Upload Page**: http://localhost:5000/upload
- **System Documentation**: http://localhost:5000/document

---

**Ready to demonstrate a fully functional, production-ready LVH detection system! 🚀**

=======
# LVH
Detection of left ventricular Hypertropy 
>>>>>>> 91c421f30704b84a049de4b322599ca7cf9aeeb6
