// ============================================
// STATS PAGE CHARTS
// Pastel color palette matching vintage theme
// ============================================

// Color palette - soft pastels
const colors = {
    sage: 'rgba(184, 212, 184, 0.8)',      // Sage green
    sageBorder: 'rgba(184, 212, 184, 1)',
    lavender: 'rgba(200, 180, 220, 0.8)',   // Soft lavender
    lavenderBorder: 'rgba(200, 180, 220, 1)',
    peach: 'rgba(250, 200, 180, 0.8)',      // Soft peach
    peachBorder: 'rgba(250, 200, 180, 1)',
    sky: 'rgba(180, 200, 220, 0.8)',        // Soft sky blue
    skyBorder: 'rgba(180, 200, 220, 1)',
    rose: 'rgba(240, 180, 190, 0.8)',       // Dusty rose
    roseBorder: 'rgba(240, 180, 190, 1)',
    cream: 'rgba(250, 235, 215, 0.8)',      // Warm cream
    creamBorder: 'rgba(250, 235, 215, 1)',
    gray: 'rgba(180, 180, 180, 0.8)',       // Soft gray
    grayBorder: 'rgba(180, 180, 180, 1)'
};

// Initialize all charts when page loads
document.addEventListener('DOMContentLoaded', function() {
    initReadingListChart();
    initRatingsChart();
    initGenresChart();
    initMonthlyChart();
});

// 1. Reading List Pie Chart
function initReadingListChart() {
    const ctx = document.getElementById('readingListChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['To Read', 'Currently Reading', 'Read'],
            datasets: [{
                data: window.statsData.readingList,
                backgroundColor: [
                    colors.sky,
                    colors.peach,
                    colors.sage
                ],
                borderColor: [
                    colors.skyBorder,
                    colors.peachBorder,
                    colors.sageBorder
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        font: {
                            size: 12
                        }
                    }
                }
            }
        }
    });
}

// 2. Star Ratings Bar Chart
function initRatingsChart() {
    const ctx = document.getElementById('ratingsChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars'],
            datasets: [{
                label: 'Number of Reviews',
                data: window.statsData.ratings,
                backgroundColor: [
                    colors.rose,
                    colors.peach,
                    colors.cream,
                    colors.lavender,
                    colors.sage
                ],
                borderColor: [
                    colors.roseBorder,
                    colors.peachBorder,
                    colors.creamBorder,
                    colors.lavenderBorder,
                    colors.sageBorder
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

// 3. Genres Horizontal Bar Chart
function initGenresChart() {
    const ctx = document.getElementById('genresChart').getContext('2d');
    
    // Create alternating pastel colors for genres
    const genreColors = window.statsData.genres.map((_, index) => {
        const colorArray = [colors.sage, colors.lavender, colors.peach, colors.sky, colors.rose];
        return colorArray[index % colorArray.length];
    });
    
    const genreBorders = window.statsData.genres.map((_, index) => {
        const colorArray = [colors.sageBorder, colors.lavenderBorder, colors.peachBorder, colors.skyBorder, colors.roseBorder];
        return colorArray[index % colorArray.length];
    });
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: window.statsData.genreLabels,
            datasets: [{
                label: 'Books Read',
                data: window.statsData.genres,
                backgroundColor: genreColors,
                borderColor: genreBorders,
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            indexAxis: 'y',
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

// 4. Monthly Progress Line Chart
function initMonthlyChart() {
    const ctx = document.getElementById('monthlyChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: window.statsData.monthLabels,
            datasets: [
                {
                    label: 'Books Read',
                    data: window.statsData.monthlyBooks,
                    borderColor: colors.sageBorder,
                    backgroundColor: colors.sage,
                    yAxisID: 'y-books',
                    tension: 0.3,
                    fill: true
                },
                {
                    label: 'Pages Read',
                    data: window.statsData.monthlyPages,
                    borderColor: colors.lavenderBorder,
                    backgroundColor: colors.lavender,
                    yAxisID: 'y-pages',
                    tension: 0.3,
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            interaction: {
                mode: 'index',
                intersect: false
            },
            plugins: {
                legend: {
                    position: 'top'
                }
            },
            scales: {
                'y-books': {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Books'
                    },
                    ticks: {
                        stepSize: 1
                    }
                },
                'y-pages': {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Pages'
                    },
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });
}